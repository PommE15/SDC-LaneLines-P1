# helper functions


def find_fit_line_points(xs, ys, y1, y2):
    # np.polyfit() returns the coefficients [A, B] of a line (y=Ax+B) 
    a, b = np.polyfit(xs, ys, 1)
    pt1 = (int(round((y1-b)/a)), int(y1))
    pt2 = (int((y2-b)/a), int(y2))
    return [pt1, pt2]


def draw_lines(img, lines, color=[255, 0, 0], thickness=2, xsize=0, ymin=0, ymax=0):
    """
    NOTE: this is the function you might want to use as a starting point once you want to 
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).  
    
    Think about things like separating line segments by their 
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of 
    the lines and extrapolate to the top and bottom of the lane.
    
    This function draws `lines` with `color` and `thickness`.    
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """
    
    min_slope = 0.176 # 10 deg, or 0.1 for 6 deg
    line_left = [[], []]
    line_right = [[], []]
    
    for line in lines:
        for x1, y1, x2, y2 in line:        
            slope = (y2-y1) / (x2-x1)
            
            # use slope and x positions to find either left or rigt line
            # not that left line is increasing and slope is negative due to the upsidedown y-axis
            
            # left
            if slope < -min_slope and x1 < xsize/2 and x2 < xsize/2:
                line_left[0].extend([x1, x2])
                line_left[1].extend([y1, y2])
                #cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 15) #test
            
            # right
            elif slope > min_slope and x1 > xsize/2 and x2 > xsize/2:
                line_right[0].extend([x1, x2])
                line_right[1].extend([y1, y2])
                #cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 15) #test
    
    # left and right
    for xs, ys in [line_left, line_right]:
        pt1, pt2 = find_fit_line_points(xs, ys, ymin, ymax)
        cv2.line(img, pt1, pt2, (255,0,0), 10)
