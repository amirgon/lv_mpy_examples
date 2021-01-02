echo "Create image directrory"
ampy mkdir images
echo "Create level directory"
ampy mkdir levels
echo "upload background images"
ampy put arkanoid_images/frame_left_9x310_rgb565.bin images/frame_left_9x310_rgb565.bin
ampy put arkanoid_images/frame_right_9x310_rgb565.bin images/frame_right_9x310_rgb565.bin
ampy put arkanoid_images/frame_top_240x10_rgb565.bin images/frame_top_240x10_rgb565.bin
echo "upload ball image"
ampy put arkanoid_images/Ball14x14_rgb565.bin images/Ball14x14_rgb565.bin
echo "upload life images"
ampy put arkanoid_images/Paddle24x8_rgb565.bin images/Paddle24x8_rgb565.bin
ampy put arkanoid_images/Paddle50x16_pressed_rgb565.bin images/Paddle50x16_pressed_rgb565.bin
ampy put arkanoid_images/Paddle50x16_released_rgb565.bin images/Paddle50x16_released_rgb565.bin
echo "upload pi image"
ampy put arkanoid_images/Pi32x32_rgb565.bin images/Pi32x32_rgb565.bin
echo "upload brick images"
ampy put arkanoid_images/Brick_Blue26x14_rgb565.bin images/Brick_Blue26x14_rgb565.bin
ampy put arkanoid_images/Brick_Green26x14_rgb565.bin images/Brick_Green26x14_rgb565.bin
ampy put arkanoid_images/Brick_Pink26x14_rgb565.bin images/Brick_Pink26x14_rgb565.bin
ampy put arkanoid_images/Brick_Red26x14_rgb565.bin images/Brick_Red26x14_rgb565.bin
ampy put arkanoid_images/Brick_Yellow26x14_rgb565.bin images/Brick_Yellow26x14_rgb565.bin
echo "upload levels"
ampy put levels/Level001.asc levels/Level001.asc
ampy put levels/Level002.asc levels/Level002.asc
ampy put levels/Level003.asc levels/Level003.asc
ampy put levels/Level004.asc levels/Level004.asc
ampy put levels/Level005.asc levels/Level005.asc
ampy put levels/Level006.asc levels/Level006.asc
ampy put levels/Level007.asc levels/Level007.asc
ampy put levels/Level008.asc levels/Level008.asc
ampy put levels/Level009.asc levels/Level009.asc
