# BIKE SHARE SYSTEM ANALYSIS PROJECT

## 🔍 More detail regarding the project
#### Note: 

## 🌐 Data Background
Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return 
back has become automatic. Currently, there are about over **500 bike-sharing programs** around the world which is composed of 
over **500 thousands bicycles**.

## ❓ Data Exploaration
1. How is the trend of bikesharing usage by registered and casual users?
2. Do users tend to use bikesharing to mobilize for going to work?
3. ***What is the peak season of bikesharing usage?***
4. How do weather affect the usage of bikesharing?

## 📊 Data Set
### Hourly Collected Data
This dataset is contained with bike sharing counts aggregated on hourly basis. Overall records of the dataset is span through **17379 hours** of data collection.
### Daily Aggregated Data
This dataset is contained with  bike sharing counts aggregated on daily basis. Overall records of the dataset is span through **731 days** of data collection

## 📊 Data Structure
- instant: record index
- dteday : date
- season : season (1:springer, 2:summer, 3:fall, 4:winter)
- yr : year (0: 2011, 1:2012)
- mnth : month ( 1 to 12)
- hr : hour (0 to 23)
- holiday : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
- weekday : day of the week
- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
  + weathersit : 
	  - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
	  - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
	  - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
	  - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
- hum: Normalized humidity. The values are divided to 100 (max)
- windspeed: Normalized wind speed. The values are divided to 67 (max)
- casual: count of casual users
- registered: count of registered users
- cnt: count of total rental bikes including both casual and registered

