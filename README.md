#Google Cloud Platform Image Recognition Algorithm

##Introduction
As a data engineer/developer, the bread and butter of the teams is the data insights that teams can syphen out of the platform to offer insights and predictions to better the entire shopify ecosystem. 

With vast amounts of images used for marketing products, shops and brand images, by identifying the objects in each image, this application (with the addition of text classifiers of course) can cluster shops with more accuracy and give insights into how and what shop owners like to put on their pages. 

The algorithm (for now) is quite simple, it takes in an image (currently only works with jpeg files) and it outputs a list of object names with their confidence values and a list of vertices circling where the object is in the image. (See examples) 

The application uses Google Cloud Platform's Vision AI image recognition algorithm, as Shopify uses GCP (at least from the job description), this should be reasonable. 

##Requirements

Python 3.7+

Google Cloud SDK https://cloud.google.com/sdk/docs/quickstart

Google Service Account Key https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances

##How to use:

###Step 1: 

Download the git repo, Copy paste your service_account.json file into the service_key.json file in the current repository

###Step 2: 
Put the images you wish to classify in the test_input folder, and modify the script to get the files

###Step 3: 
Run the script, and your file should be in the ouput.txt file, you may modify the script to reroute the output.txt file or write into a database


##Potential Next Steps 
1. Larger Volumes of images (read from database, run script, write to database) 
2. Data Visualization (Get more insights e.g. What image is used the most for X cluster) 
3. GUI or better frontend 
4. Orchastration, scheduled updates to get new images on a daily basis (Airflow or Kubeflow)
5. Combine result with text classifiers (vectorize the result with text classifiers to improve on the algorithm) 
6. Use of big data tools to multithread the process (although I'm not sure if GCP can handle big data ML, need further testing) 


##Sample 

Input: 

![picture](test_input/test_5.jpeg)

Output: 

Number of objects found: 10
Watch (confidence: 0.9202269315719604)Normalized bounding polygon vertices:  - (0.13823191821575165, 0.1626967340707779) - (0.2276538461446762, 0.1626967340707779) - (0.2276538461446762, 0.4611910581588745) - (0.13823191821575165, 0.4611910581588745)
Watch (confidence: 0.9191744923591614)Normalized bounding polygon vertices:  - (0.019053377211093903, 0.5680782198905945) - (0.25602054595947266, 0.5680782198905945) - (0.25602054595947266, 0.734943151473999) - (0.019053377211093903, 0.734943151473999)
Person (confidence: 0.9110227227210999)Normalized bounding polygon vertices:  - (0.47731050848960876, 0.7391592860221863) - (0.6444106698036194, 0.7391592860221863) - (0.6444106698036194, 0.9962978959083557) - (0.47731050848960876, 0.9962978959083557)
Person (confidence: 0.9059911966323853)Normalized bounding polygon vertices:  - (0.8492130637168884, 0.7475652098655701) - (0.9941837191581726, 0.7475652098655701) - (0.9941837191581726, 0.992985725402832) - (0.8492130637168884, 0.992985725402832)
Person (confidence: 0.9014054536819458)Normalized bounding polygon vertices:  - (0.15933024883270264, 0.7391183972358704) - (0.3092644512653351, 0.7391183972358704) - (0.3092644512653351, 0.9961052536964417) - (0.15933024883270264, 0.9961052536964417)
Person (confidence: 0.9001266956329346)Normalized bounding polygon vertices:  - (0.275971919298172, 0.12811927497386932) - (0.9223171472549438, 0.12811927497386932) - (0.9223171472549438, 0.7218050956726074) - (0.275971919298172, 0.7218050956726074)
Sunglasses (confidence: 0.8906610608100891)Normalized bounding polygon vertices:  - (0.501814067363739, 0.10372335463762283) - (0.622297465801239, 0.10372335463762283) - (0.622297465801239, 0.2740924060344696) - (0.501814067363739, 0.2740924060344696)
Outerwear (confidence: 0.8715665936470032)Normalized bounding polygon vertices:  - (0.4838716685771942, 0.8512343764305115) - (0.6404725909233093, 0.8512343764305115) - (0.6404725909233093, 0.9973958134651184) - (0.4838716685771942, 0.9973958134651184)
Top (confidence: 0.8490291237831116)Normalized bounding polygon vertices:  - (0.8530711531639099, 0.8509180545806885) - (0.984931230545044, 0.8509180545806885) - (0.984931230545044, 0.9932665824890137) - (0.8530711531639099, 0.9932665824890137)
Top (confidence: 0.81346195936203)Normalized bounding polygon vertices:  - (0.16125506162643433, 0.8715503811836243) - (0.30010858178138733, 0.8715503811836243) - (0.30010858178138733, 0.99542635679245) - (0.16125506162643433, 0.99542635679245)



