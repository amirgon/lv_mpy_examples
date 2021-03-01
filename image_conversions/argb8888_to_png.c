#include <png.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
/*
 * a program to create a png file from raw argb8888 data
 * created for a project with the course of embedded systems 
 * at the University of Cape Coast, Ghana
 * Author: U. Raich, 25. 2. 2021
 * This program is released under the MIT license
 */    
#define ERROR -1


int main (int argc, char **argv)
{
    FILE *inFile,*outFile;
    char *outfileName,*filenameRest;
    int fileSize,width,height,x,y;
    int pixel_size = 4;
    uint8_t *inbuf,*inbufPtr,red,green,blue,opacity;

    png_structp png_ptr = NULL;
    png_infop info_ptr = NULL;
    png_byte ** row_pointers = NULL;
    /* "status" contains the return value of this function. At first
       it is set to a value which means 'failure'. When the routine
       has finished its work, it is set to a value which means
       'success'. */
    int status = -1;
    int depth = 8;
    /* The following number is set by trial and error only. I cannot
       see where it it is documented in the libpng manual.
    */
    status = 0;

    if (argc != 4) {
      printf("Usage: %s filename_argb8888.bin width height\n",argv[0]);
      exit(-1);
    }

    outfileName = malloc(strlen(argv[1]));
    strcpy(outfileName,argv[1]);
    if ((filenameRest=strstr(outfileName,"_argb8888.bin")) == NULL) {
      printf("outfileName: %s\n",outfileName);
      printf("File must be named xxx_argb8888.bin\n");
      exit(-1);
    }
    printf("filename ext: %s\n",filenameRest);
    strcpy(filenameRest,"_argb8888.png");
    printf("Output file name: %s\n",outfileName);
    width = atoi(argv[2]);
    height = atoi(argv[3]);
    printf("width: %d, height: %d\n",width,height);      
    if ((inFile = fopen(argv[1],"r")) == NULL)
      fprintf(stderr,"Could not open the %s file for reading\n",argv[1]);
    printf("raw image file successfully opened for reading\n");
    
    fseek(inFile, 0L, SEEK_END);
    fileSize = ftell(inFile);
    printf("file size: %d\n",fileSize);
    rewind(inFile);
    inbuf = malloc(fileSize);
    /*
      read the raw data
    */
    fread(inbuf, fileSize, 1, inFile);
    fclose(inFile);

    if ((outFile = fopen(outfileName,"w")) == NULL)
      fprintf(stderr,"Could not open the %s file for writing\n",outfileName);
    printf("png image file successfully opened for writing\n");
    
    png_ptr = png_create_write_struct (PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
    if (png_ptr == NULL) {
      printf("png_create_write_struct_failed\n");
      return ERROR;
    }
    else
      printf("png write structure successfully created\n");
    
    info_ptr = png_create_info_struct (png_ptr);
    if (info_ptr == NULL) {
      printf("png_create_info_struct_failed\n");
      return ERROR;
    }
    else
      printf("png info structure successfully created\n");
    /* Set up error handling. */

    if (setjmp (png_jmpbuf (png_ptr))) {
      printf("long jmp error\n");
      return ERROR;
    }
    
    /* Set image attributes. */

    png_set_IHDR (png_ptr,
                  info_ptr,
                  width,
                  height,
                  depth,
                  PNG_COLOR_TYPE_RGB_ALPHA,
                  PNG_INTERLACE_NONE,
                  PNG_COMPRESSION_TYPE_DEFAULT,
                  PNG_FILTER_TYPE_DEFAULT);

    /* Initialize rows of PNG. */

    row_pointers = png_malloc (png_ptr, height * sizeof (png_byte *));
    /* copy the pixel data */
    inbufPtr = inbuf;
    for (y = 0; y < height; y++) {
        png_byte *row = 
            png_malloc (png_ptr, sizeof (uint8_t) * width * pixel_size);
        row_pointers[y] = row;
        for (x = 0; x < width; x++) {
	  red     = *inbufPtr++;
	  green   = *inbufPtr++;
	  blue    = *inbufPtr++;
	  opacity = *inbufPtr++;
	  *row++ = blue; 
	  *row++ = green;
	  *row++ = red; 
	  *row++ = opacity; 
        }
    }
    
    /* Write the image data to "outFile". */

    png_init_io (png_ptr, outFile);
    png_set_rows (png_ptr, info_ptr, row_pointers);
    png_write_png (png_ptr, info_ptr, PNG_TRANSFORM_IDENTITY, NULL);

    /* The routine has successfully written the file, so we set
       "status" to a value which indicates success. */

    status = 0;
    
    for (y = 0; y < height; y++) {
        png_free (png_ptr, row_pointers[y]);
    }
    png_free (png_ptr, row_pointers);
     
    fclose(outFile);
    return status;
}
