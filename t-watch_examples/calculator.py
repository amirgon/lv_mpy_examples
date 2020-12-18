#!/opt/bin/lv_micropython -i -i
import lvgl as lv
import display_driver

class Calculator():
    op1_text="0"
    op2_text="0"
    op_num=0

    digits="0123456789"
    operators=["+","-","x","/"]
    dec_point = False
    operator = None
    resultFlag = False
    btnm_map = ["7","8", "9", "/", " ","\n",
                "4", "5", "6", "x", lv.SYMBOL.BACKSPACE, "\n",
                "1", "2", "3","+","=","\n",
                "c","0",".","-"," ",""]

    btnm_ctlr_map = [lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.HIDDEN,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.NO_REPEAT,
                     lv.btnmatrix.CTRL.HIDDEN]

    def __init__(self,parent):
        # create the number textarea
        self.ta = lv.textarea(parent,None)
        self.ta.set_size(200,40)
        self.ta.align(None,lv.ALIGN.IN_TOP_MID,0,10)
        self.ta.set_text("0")

        # create a button matrix
        self.btnm = lv.btnmatrix(parent,None)
        self.btnm.set_map(self.btnm_map)
        self.btnm.set_ctrl_map(self.btnm_ctlr_map)
        self.btnm.set_width(226)
        self.btnm.align(self.ta,lv.ALIGN.OUT_BOTTOM_MID,0,10)
        # attach the callback
        self.btnm.set_event_cb(self.event_handler)
        
    def event_handler(self,source,evt):

        if evt == lv.EVENT.VALUE_CHANGED:
            print("Toggled")
            txt = source.get_active_btn_text()
            #
            # treat digits
            #
            if txt in self.digits:
                print("digit: ",txt)
                if self.resultFlag:
                    self.op_num = 0
                    self.resultFlag = False
                    self.op1_text="0"
                    self.op2_text="0"
                if self.op_num == 0:
                    if self.op1_text == "0":
                        self.op1_text = txt
                    else:
                        self.op1_text = self.op1_text + txt
                    self.ta.set_text(self.op1_text)                    
                else:
                    if self.op2_text == "0":
                        self.op2_text = txt
                    else:
                        self.op2_text = self.op2_text + txt                
                    self.ta.set_text(self.op2_text)

            #
            # treat decimal point
            #
            elif txt == ".":
                if self.dec_point:
                    print ("decimal point was already typed")
                    return
                else:
                    print("decimal point")
                    self.dec_point=True
                if self.op_num == 0:
                    self.op1_text = self.op1_text + txt
                    self.ta.set_text(self.op1_text)
                else:
                    self.op2_text = self.op2_text + txt
                    self.ta.set_text(self.op2_text)
                    
            elif txt == lv.SYMBOL.BACKSPACE:
                print("backspace")
                if self.op_num == 0:
                    if self.op1_text == "0":
                        return
                    else:
                        removedChar = self.op1_text[-1:]
                        if removedChar == '.':
                            self.dec_point = False
                        self.op1_text = self.op1_text[:-1]
                        self.ta.set_text(self.op1_text)
                else:
                    if self.op2_text == "0":
                        return
                    else:
                        removedChar = self.op2_text[-1:]
                        if removedChar == '.':
                            self.dec_point = False
                        self.op2_text = self.op2_text[:-1]
                        self.ta.set_text(self.op2_text)                   
                    
            elif txt == "c":
                print("clear")
                if self.op_num == 0:
                    self.op1_text = "0"
                    self.ta.set_text(self.op1_text)
                else:
                    self.op2_text = "0"
                    self.ta.set_text(self.op2_text)
                operator=None
                dec_point=False
            
            elif txt == "=":
                print("Calculate result of operation: ",self.op1_text,self.operator,self.op2_text)
                if self.operator in self.operators:
                    op1 = float(self.op1_text)
                    op2 = float(self.op2_text)
                    print("op1: %f, op2: %f"%(op1,op2))
                    if self.operator == "+":
                        print(op1,self.operator,op2)                    
                        result = op1 + op2
                        res_text = str(result)
                        self.op2_text = "0"
                        self.op1_text = res_text
                        print(op1,self.operator,op2)
                    
                    elif self.operator == "-":
                        print(op1,self.operator,op2)                    
                        result = op1 - op2
                        res_text = str(result)
                        self.op2_text = "0"
                        self.op1_text = res_text

                    elif self.operator == "x":
                        print(op1,self.operator,op2)                    
                        result = op1 * op2
                        res_text = str(result)
                        self.op2_text = "0"
                        self.op1_text = res_text
                        
                    elif self.operator == "/":
                        print(op1,self.operator,op2)  
                        if op2 == 0:
                            res_text = "NaN"
                        else:
                            result = op1 / op2
                            res_text = str(result)
                            self.op2_text = "0"
                            self.op1_text = res_text
                            
                    print("result text: ", res_text)    
                    self.ta.set_text(res_text)
                    self.operator = None
                    self.resultFlag=True
                    if res_text == "NaN":
                        self.resultFlag=False
                        self.op1_text="0"
                        self.op_num = 0
                        self.op2_text="0"
                
            else:
                print("Operator: ",txt)
                self.resultFlag=False
                if self.operator:
                    print("operator already selected")
                else:
                    self.op_num=1
                    self.dec_point=False
                    self.operator = txt
                    self.ta.set_text(self.op2_text)


# create a calculator
calc = Calculator(lv.scr_act())

