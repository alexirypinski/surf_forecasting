# Surf Forecasting: Understanding wave activity in an area with complex bathymetry

Since I started surfing at the age of five, I've been fascinated by the physical dynamics that drive waves around my local surf spots around San Diego. Perhaps the most interesting area of San Diego in terms of wave dynamics is my home break at Blacks beach and the nearby surf spot at Scripps. At Blacks, Open ocean swells roll out of a deep canyon from the south and intersect waves coming from the north to form thick, hollow peaks that explode onto a shallow sand shelf. Yet only a hundred feet south of the main break, the ocean almost always resembles a lake. 

**Why is this?** As I grew older, I began to understand that the canyon that creates the magical waves at Blacks beach has enormous effects on the wave activity of surrounding areas. Open ocean waves with longer periods and more energy feel friction against the ocean floor that slows them down -- however, this friction is absent in places with deeper water. Thus, waves will propagate faster in deeper water, and change directions following the contours of the ocean floor. In the case of the Scripps Submarine Canyon, the faster moving wave energy will bend along the canyon and land on the beach directly at Blacks and away from areas to the south such as Scripps and La Jolla Shores. Here's an illustration of this phenomenon:

![alt text](https://pv-lab.org/wp-content/uploads/2018/01/refdif.gif)


But the dynamics of refraction are complex -- depending on a huge amount of obscure interactions of different variables. To make matters worse, offshore islands selectively block many swell directions that a priori are are hard to understand. When there is even a small amount of refraction due to complex bathymetry, the relationship between offshore swell height and nearshore swell height is highly nonlinear. For the purposes of surf forecasting, it is impossible to capture the essence of this stretch of coast in terms of linear models. For this project, I wanted to see how well certain machine learning models could capture the hidden relationships that make this place so unpredictable.  

#What's the data? 

The data is publically available NOAA offshore buoy data. Unfortunately, there are no nearshore buoys at Blacks beach, which is where I was most interested in studying. There is, however, a buoy that gives detailed wave measurements on the pier at Scripps (buoy numper LJPC1), which is located less than 200 feet from the beginning of the Scripps Canyon. The buoy whose data I am using as the basis of my measurements is the Torrey Pines Offshore buoy (buoy number). This buoy's measurements were selected to be the unique predictor of wave activity at scripps 




#What's the model? 
There are several models. 


#What are the results? 

As of February 2, 2021 I am still testing models and creating presentable representations of the results in matplotlib. Bear with me. I'll have them soon. It appears that my MLP network was hightly successful. 


