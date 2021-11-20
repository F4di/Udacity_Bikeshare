import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Please type which city you want your data from (chicago, new york city, washington): ").lower()
            if city in CITY_DATA:
                break;
            else:
                print('Please type only one of the cities as written above')
        except:
            print('Please type only one of the cities as written above')
            continue


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Please type which month (january, february, march, april, may, june) or all: ").lower()
            if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                break;
            else:
                print('Please type only one of the months in letters as written above or all to consider all months')
        except:
            print('Please type only one of the months in letters as written above or all to consider all months')
            continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("please specify which day of week (sunday, monday, tuesday, wednesday, thursday, friday, saturday) or all: ").lower()
            if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursdaay', 'friday', 'saturday', 'all']:
                break;
            else:
                print('Please type one day of week in letters as written above or all to choose all days')
        except:
            print('Please type one day of week in letters as written above or all to choose all days')
            continue



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode().iat[0]
    print('Most Frequent month:', common_month)
    print()

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode().iat[0]
    print('Most Frequent day:', common_day)
    print()


    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().iat[0]
    print('Most Frequent Start Hour:', popular_hour)
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode().iat[0]
    print('Most commonly used start station:', common_start_station)
    print()

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode().iat[0]
    print('Most commonly used end station:', common_end_station)
    print()

    # TO DO: display most frequent combination of start station and end station trip
    common_startend_station = (df['Start Station'] + ' -with- ' + df['End Station']).mode()[0]
    print('Most commonly combination of start station and end station:', common_startend_station)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    print()
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('total travel time is:', trip_duration)
    print()

    # TO DO: display mean travel time
    trip_average = df['Trip Duration'].mean()
    print('average travel time is:', trip_average)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    print()
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types:', user_types)
    print()

    # TO DO: Display counts of gender    
    try:
        user_gender = df['Gender'].value_counts()
        print('counts of user gender:', user_gender)
        print()
    except:
        print('Can not count users genders because it is not in the data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = df['Birth Year'].min()
        print('earliest year of birth:', earliest_birthyear)
        print()
    except:
        print('Can not specify earliest year of birth because it is not in the data.')
    try:    
        mostrecent_birthyear = df['Birth Year'].max()
        print('most recent year of birth:', mostrecent_birthyear)
        print()
    except:
        print('Can not specify most recent year of birth because it is not in the data.')
    try:    
        mostcommon_birthyear = df['Birth Year'].mode()[0]
        print('most common year of birth:', mostcommon_birthyear)
        print()
    except:
        print('Can not specify most common year of birth because it is not in the data.')
        print()
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def more_data(df):
    
    """ Displays 1 more row data, returns None."""
    
    valid_answers = ['yes', 'no']
    counter = 0
    ind_data = ''
    while True:
        if ind_data.lower() not in valid_answers:
            print("\nPlease type a valid answer")
            ind_data = input('would you like to see more data? type yes or no\n')
        elif ind_data.lower() == 'yes':
            print(df[counter:counter+5])
            counter += 5
            ind_data = input('would you like to see more data? type yes or no\n')
        elif ind_data.lower() == 'no':
            break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
