INSTALLATION:

python version - 3.5.2
pip3 version   - 8.1.1

sudo apt update

sudo apt install python3-dev python3-pip

sudo pip3 install -U virtualenv  # system-wide install

virtualenv --system-site-packages -p python3 ./venv

source venv/bin/activate

pip install opencv-python

pip install --upgrade tensorflow

pip install pandas

pip install youtube-dl

_______________________________________________________
BASH scripts are used to download the data from youtube dataset

youtube8mcategories.txt - represents all approximately 4000 categoies.

bash downloadmulticategoryvideos.sh <number-of-videos-per-category> <selected-category-file-name>
bash downloadmulticategoryvideos.sh 2 selected_categories.txt

At First selected categories used are from 
Indoor categories : Bedroom, House, Hotel, Classroom, Office)

Then Ran the same bash command for outdoor categories:
Indoor categories : Outdoor Recreation, Landscape, Mountain, Beach

This downloads 12 videos in each categories. 
The reason to use bash script is youtube8m dataset website contains information to use their data using tensorflow protocol buffers, which was making harder for me to extract images from videos.

downloadvideos.sh - bash commands included here based on on youtube8m data website on how to used video-ids to download the youtube video using a specific url. https://research.google.com/youtube8m/video_id_conversion.html

------------------------------------------------------------------------------
CREATE FRAMES:

At this point, there are 7-8 videos in each category. removed few few videos because of too many frames.

create_frames.py - is used to create frames using the videos downloaded in the last step. 
now we have our training data for indoor and outdoor frames.

-------------------------------------------------------------------------------------
DOWNLOAD tensor-flow-for-poets-2 for creating a neural network for indentiying images to be a indoor or outdoor.

cd tensor-flow-for-poets-2

move the data under tf_files
$ tf_files/indoor - will have indoor images
$ tf_files/outdoor - will have outdoor images

create ENV variables:
IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

RUN:
python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=tf_files
  
this will create bottlenecks directory, 
retrained_graph.pb  - is the nn model
retrained_labels.txt - contains the categories

-----------------------------------------------------------------------------------------
TEST THE category of new image using:
python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=test_data/frames_0.jpg






_____________________________________________________________
