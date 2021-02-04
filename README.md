# Surf Forecasting: Understanding wave activity in an area with complex bathymetry

Note: currently importing code from a prototype IPYNB -- most of the files are not yet functional

Since I started surfing at the age of five, I've been fascinated by the physical dynamics that drive waves around my local surf spots around San Diego. Perhaps the most interesting area of San Diego in terms of wave dynamics is my home break at Blacks beach and the nearby surf spot at Scripps. At Blacks, Open ocean swells roll out of a deep canyon from the south and intersect waves coming from the north to form thick, hollow peaks that explode onto a shallow sand shelf. Yet only a hundred feet south of the main break, the ocean almost always resembles a lake. 

**Why is this?** As I grew older, I began to understand that the canyon that creates the magical waves at Blacks beach has enormous effects on the wave activity of surrounding areas. Open ocean waves with longer periods and more energy feel friction against the ocean floor that slows them down -- however, this friction is absent in places with deeper water. Thus, waves will propagate faster in deeper water, and change directions following the contours of the ocean floor. In the case of the Scripps Submarine Canyon, the faster moving wave energy will bend along the canyon and land on the beach directly at Blacks and away from areas to the south such as Scripps and La Jolla Shores. Here's an illustration of this phenomenon:

![alt text](https://pv-lab.org/wp-content/uploads/2018/01/refdif.gif)


But the dynamics of refraction are complex -- depending on a huge amount of obscure interactions of different variables. To make matters worse, offshore islands selectively block many swell directions that a priori are are hard to understand. When there is even a small amount of refraction due to complex bathymetry, the relationship between offshore swell height and nearshore swell height is highly nonlinear. For the purposes of surf forecasting, it is impossible to capture the essence of this stretch of coast in terms of linear models. For this project, I wanted to see how well certain machine learning models could capture the hidden relationships that make this place so unpredictable.  

# What's the data? 

The data is four years of publically available NOAA offshore buoy data. Unfortunately, there are no nearshore buoys at Blacks beach, which is where I was most interested in studying. There is, however, a buoy that gives detailed wave measurements on the pier at Scripps (buoy numper LJPC1), which is located less than 200 feet from the beginning of the Scripps Canyon. The buoy whose data I am using as the basis of my measurements is the Torrey Pines Offshore buoy (buoy number 46224). This buoy's measurements were selected to be the unique predictor of wave activity at Scripps for three reasons.

  1. It is at the head of the Scripps Canyon directly to the northwest of scripps, before waves have experienced significant refraction.
  2. It has a similar swell fetch to the Scripps buoy. Other buoys to the north and south experience significant island and headland blockage. I believe that including them as model features would only create noise.
  3. It has detailed information going back longer than other nearby buoys. 
  
The data from the buoys consisted of over a hundred thousand hourly observations indexed by time. They recorded many types of information, but only several variables were actually relevant. These were: 

  1. The significant wave height: the average of the top 1/3rd of waves between observations. 
  2. Average wave period: the average of the wave periods present in the wave spectrum.
  3. Dominant wave period: the period of the dominant swell
  4. Mean wave direction: the mean of the different directions of swell hitting the buoy.
  
 Man, it would be nice if the NOAA kept full spectral data of period, wave direction, and height. It would make predictions so much more accurate. Unfortunately, this is what we have to work with, so we'll make the best of it. 
  
 
  
## Cleaning and Exploratory Analysis 

Despite being relatively well maintained, these datasets still proved to be a pain to work with and tested the limits of my 'wizardry' in Python. Nonetheless, I learned a lot -- especially about the importance of optimizing operations on Pandas dataframes and knowing how these operations work on the C level. This solidified my understanding of proper Python workflows on large datasets and was immensely valuable. 

The hardest part of assembling my training, validation, and testing datasets was matching observations from the two buoys into feature-label pairings because the times that the observations were recorded between the two buoys often did not match up. This challenge took me a few days to overcome, as I wrangled with missing data and intractable polynomial runtimes. Eventually, I chose a simple solution that worked well enough not to add noise to my data, but avoided large runtimes. 




# What's the model? 
There are several models. 

### Linear Model 1
My first model is a linear model on the four relevant buoy observations (significant wave height, dominant period, average period, mean wave direction). I chose to implement this algorithm in PyTorch with stochastic gradient descent instead of using the closed form solution for linear regression as a sanity check. It obviously doesn't work too well. 


### Linear Model 2
My next model is a linear model on the four relevant buoy observations plus two derived variables.

Waves will start to experience shoaling (interactions with the ocean floor) at a depth proportional to the square of their period. Shoaling means refraction, which means that waves of greater average period will lose much of their height by the time they arrive at Scripps from offshore. Thus, I decided to include the square of average period into my model.

The next variable is the ratio of dominant period to average period. This captures in some sense the tendency for the wave period spectrum on the buoy to have many periods, both short and long. This means that some of the swell will not be filtered by the Scripps Canyon. 

Obviously, in a linear model, many of these variables will be highly correlated and will thus add noise and inaccuracy. However, in a neural network model, hidden nonlinear interactions between these features will be understood.

## Perceptron Model 1
This is a neural network with 3 fully connected hidden layers which are all of size 6. Since this is a pretty shallow network, I am not worried about exploding gradients, so I am using a sigmoid activation function instead of ReLUs or leaky ReLUS.

Due to the nature of swell events tending to be quite unique (at least over a period of 5 years), I am extremely worried about overfitting. Thus, I'm using L2 weight regularization. I'm also training the network using a dropout of 0.2 on the input layer and 0.4 on the other layers. 

I'm trying out the ADAM algorithm to train this network. Right now, I am not too worried about tuning the hyperparameters and instead worried about convergence. 


## Perceptron Model 2
This is a neural network with 5 fully connected hidden layers which are all of size 6. Still debugging convergence.


# What are the results? 

As of February 2, 2021 I am still creating presentable representations of the results in matplotlib. Bear with me. I'll have them soon.

# Future work

I want to:

Tune the hyperparameters on my perceptron models.
Make the results more presentable (gotta improve my data visualization skills)
Do PCA on my dataset and use that to improve my model.






