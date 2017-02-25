# TODO: Build your pipeline that will draw lane lines on the test_images
# then save them to the test_images directory.


# variables
kernel_size = 5      # Must be an odd number (3, 5, 7...)
low_threshold = 40   # 50
high_threshold = 120 # 150

rho = 2              # distance resolution in pixels of the Hough grid
theta = np.pi/180    # angular resolution in radians of the Hough grid
threshold = 6        # minimum number of votes (intersections in Hough grid cell)
min_line_length = 18 # minimum number of pixels making up a line
max_line_gap = 6     # maximum gap in pixels between connectable line segments

images = os.listdir("test_images/")


def lane_detect_image(index):

    # read file
    image = mpimg.imread('test_images/' + images[index])
    return lane_detect(image)
    
    
def lane_detect(image):

    # 1. Canny Edge Detection
    # - grayscale
    # - gaussian blur
    # - edges
    gray = cv2.cvtColor(np.copy(image), cv2.COLOR_RGB2GRAY)
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)


    # 2. Region Mask
    xsize = image.shape[1]
    ysize = image.shape[0]
    ymax = ysize
    ymin = (ysize/2)+55
    point_lb = (0, ymax)
    point_lt = ((xsize/2)-15, ymin)
    point_rt = ((xsize/2)+15, ymin)
    point_rb = (xsize, ymax)

    vertices = np.array([[point_lb, point_lt, point_rt, point_rb]], dtype=np.int32)
    mask = np.zeros_like(edges)   
    ignore_mask_color = 255 

    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_edges = cv2.bitwise_and(edges, mask)


    # 3. Hough Transform to Find Lines
    # create a blank to draw lines on
    line_image = np.copy(image)*0   
    lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    
    
    # draw image
    draw_lines(line_image, lines, [255, 0, 0], 10, xsize, ymin, ymax)
    image_lane = cv2.addWeighted(image, 0.8, line_image, 1, 0) 
    
    return image_lane
