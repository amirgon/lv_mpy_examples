'''
Original author: mhepp(https://forum.lvgl.io/u/mhepp/summary)
Transformed into a class: uraich
'''

import lvgl as lv
import uerrno
import ustruct as struct

class Fs_driver():
    def __init__(self):
        fs = None
    
    def fs_open_cb(self,drv, fs_file, path, mode):

        p_mode = ''
        if mode == 1:
            p_mode = 'wb'
        elif mode == 2:
            p_mode = 'rb'
        elif mode == 3:
            p_mode = 'rb+'
            
        if p_mode == '':
            print("fs_open_callback() - open mode error, {} is invalid mode".format(mode))
            return lv.FS_RES.INV_PARAM
            
        cast_fs = lv.fs_file_t.cast(fs_file)
        print("Trying to open: " + path)
        try:
            self.fd  = open(path, p_mode)
        
        except Exception as e:
            print("fs_open_callback() exception: ", uerrno.errorcode[e.args[0]])
            return lv.FS_RES.FS_ERR

        print("open successful")
        return lv.FS_RES.OK


    def fs_close_cb(self,drv, fs_file):
        
        try:
            self.fd.close()
        except Exception as e:
            print("fs_close_callback() exception ", uerrno.errorcode[e.args[0]])
            return lv.FS_RES.FS_ERR

        return lv.FS_RES.OK


    def fs_read_cb(self,drv, fs_file, buf, btr, br):
        #cast_fs = lv.fs_file_t.cast(fs_file)

        try:
            tmp_data=self.fd.read(btr)
            #tmp_data = cast_fs.file_d.cast()['file'].read(btr)
            # tmp_len = len(tmp_data)
            buf.__dereference__(btr)[0:len(tmp_data)] = tmp_data
            br.__dereference__(4)[0:4] = struct.pack("<L", len(tmp_data))

        except Exception as e:
            print("fs_read_callback() exception ", uerrno.errorcode[e.args[0]])
            return lv.FS_RES.FS_ERR

        return lv.FS_RES.OK


    def fs_seek_cb(self,drv, fs_file, pos):
        # cast_fs = lv.fs_file_t.cast(fs_file)

        try:
            # to =
            # cast_fs.file_d.cast()['file'].seek(pos, 0)
            self.fd.seek(pos, 0)
        except Exception as e:
            print("fs_seek_callback() exception ", uerrno.errorcode[e.args[0]])
            return lv.FS_RES.FS_ERR
        
        return lv.FS_RES.OK
    
    
    def fs_tell_cb(self, drv, fs_file, pos):
        # cast_fs = lv.fs_file_t.cast(fs_file)
        
        try:
            tpos = self.fd.tell()
            #tpos = cast_fs.file_d.cast()['file'].tell()
            pos.__dereference__(4)[0:4] = struct.pack("<L", tpos)
        except Exception as e:
            print("fs_tell_callback() exception ", uerrno.errorcode[e.args[0]])
            return lv.FS_RES.FS_ERR
        
        return lv.FS_RES.OK


    def fs_write_cb(self, drv, fs_file, buf, btw, bw):
        # cast_fs = lv.fs_file_t.cast(fs_file)
        
        try:
            wr = self.fd.write(buf[0:btw])
            #wr = cast_fs.file_d.cast()['file'].write(buf[0:btw])
            bw.__dereference__(4)[0:4] = struct.pack("<L", wr)
        except Exception as e:
            print("fs_write_callback() exception ", uerrno.errorcode[e.args[0]])
            return lv.FS_RES.FS_ERR
        
        return lv.FS_RES.OK


    def fs_register(self, fs_drv, letter):

        fs_drv.init()
        fs_drv.letter = ord(letter)
        fs_drv.open_cb = self.fs_open_cb
        fs_drv.read_cb = self.fs_read_cb
        fs_drv.write_cb = self.fs_write_cb
        fs_drv.seek_cb = self.fs_seek_cb
        fs_drv.tell_cb = self.fs_tell_cb
        fs_drv.close_cb = self.fs_close_cb
        
        fs_drv.register()
        print("fs_driver registered!")
