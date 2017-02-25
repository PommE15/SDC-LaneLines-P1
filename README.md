# SDC-LaneLines-P1
Finding Lane Lines on the Road

## Instruction
https://github.com/udacity/CarND-LaneLines-P1/blob/master/P1.ipynb

## Implementation
Build your pipeline that will detect and draw lane lines on the test images

## Result

## Reflections
### How could you imagine making your algorithm better / more robust?
- weight on potiential lane colors
- remove noises such as too short lines with outlier slope degrees
- mask interest regions dynamically with help of other CV techniques

### Where will your current algorithm be likely to fail?
In general, this algorithm fails in two cases:
- noise objects in the mask regions
- the car is not approximately driving in the center of the lane,

for example:

- when the lane has signs painted, trash, and whatever things on the ground
- when there are others cars in the front, or like in the challenge.mp4 that the head of the car is in the video clips
- when the car is in a turn, roundabout, or changing lanes

Last but not least thought is how to balance parameter tweeking and not over tuning to fit in specific cases as I only tested this algorithm in three video clips.
