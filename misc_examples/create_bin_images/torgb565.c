/* Convert the blueflower 32bit image file to rgb565 */

#include <stdio.h>
#include <stdlib.h>
int main(int argc, char ** argv){
  FILE *infile,*outfile;
  unsigned char *inbuf,*outbuf,*inbufPtr,*outbufPtr;
  unsigned char red,green,blue,opacity,col_high_byte,col_low_byte;
  int fileSize,i;

  infile = fopen("blue_flower_32.bin","r");
  if (infile == NULL) {
    printf("Could not open blue_flower.bin");
    exit(-1);
  }

  fseek(infile, 0L, SEEK_END);
  fileSize = ftell(infile);
  printf("file size: %d\n",fileSize);
  rewind(infile);

  inbuf = malloc(fileSize);
  outbuf = malloc(fileSize*3/4);
  
  fread(inbuf, fileSize, 1, infile);
  fclose(infile);
    
  for (i=0; i<16;i++)
    printf("0x%02x ",inbuf[i]);
  printf("\n");
    
  inbufPtr = inbuf;
  outbufPtr = outbuf;
  for (i=0;i<fileSize/4;i++) {
// for (i=0;i<1;i++) {
    red = *inbufPtr++;
    green = *inbufPtr++;
    blue = *inbufPtr++;
    opacity = *inbufPtr++;

    red &=0xf8;
    green &=0xfc;
    blue &=0xf8;
    col_high_byte = blue | (green & 0xe0) >> 5;
    col_low_byte = (green & 0x1c) << 3 | red >> 3;
    //    printf("red: 0x%02x, green: 0x%02x, blue: 0x%02x, high: 0x%02x, low: 0x%02x\n",
    //	   red,green,blue,col_high_byte,col_low_byte);

    *outbufPtr++ = col_high_byte;
    *outbufPtr++ = col_low_byte;
    *outbufPtr++ = opacity;
  }
  outfile = fopen("blue_flower_rgb565.bin","w");
  if (outfile == NULL) {
    printf("Could not open blue_flower_rgb565.bin");
    exit(-1);
  }
  fwrite(outbuf, fileSize*3/4, 1, outfile);
  fclose(outfile);
    
}
