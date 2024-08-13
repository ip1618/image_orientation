Algorithm: 
1. Bounding Box Detection
   The algorithm starts by taking an input image and uses Google Vision to detect the bounding boxes around the car and its tires. This information is crucial for determining the orientation of the image.

2. Orientation Calculation
   Using the Euclidean distance, the algorithm identifies the orientation of the bounding box. For a correctly oriented (horizontal) image, the longest side of the bounding box should be parallel to the x-axis. The algorithm calculates the angle of rotation needed to achieve this orientation.

3. Rotation and Validation
   The calculated angle of rotation may result in two possible orientations: one completely flipped and one correct. To determine the correct orientation, the algorithm:
   - Finds the original centroid of the bounding box.
   - Computes the average height of the tires in the image.
   - Applies a rotation matrix to transform these points into the new coordinate system.
   - Compares the new average height of the tires with the new centroid after rotation. The image where the new average height of the tires is less than the new centroid is identified as the correct orientation.

4. Final Output
   The correctly oriented image is saved, and any necessary adjustments are applied.