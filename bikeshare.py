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
    print('Hi! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city not in CITY_DATA.keys():
            print('Invalid input. Please try again.')
            continue
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    filter_choice = ''
    while filter_choice not in ['month', 'day', 'both', 'none']:
        filter_choice = input("Would you like to filter the data by month, day, both or none? ").lower()
        if filter_choice not in ['month', 'day', 'both', 'none']:
            print("Invalid input. Please enter 'month', 'day', 'both', or 'none'.")

    if filter_choice == 'month' or filter_choice == 'both':
        month = ''
        while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            month = input("Which month - January, February, March, April, May, or June? ").lower()
            if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                print("Invalid input. Please enter a valid month or 'all'.")
    else:
        month = 'all'

    if filter_choice == 'day' or filter_choice == 'both':
        day = ''
        while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").lower()
            if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                print("Invalid input. Please enter a valid day of the week or 'all'.")
    else:
        day = 'all'

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

    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month of travel is: {common_month}")
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of travel is: {common_day}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print(f"The most common start hour is: {common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {common_start_station}")
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {common_end_station}")


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' - ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print(f"The most frequent combination of start station and end station trip is: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is: {total_travel_time/3600} hours.")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is: {mean_travel_time/60} minutes.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)


    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:\n", gender_counts)
    else:
        print("\nGender data not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        earliest_year = int(birth_year.min())
        most_recent_year = int(birth_year.max())
        most_common_year = int(birth_year.mode()[0])
        print('\nEarliest Birth Year:', earliest_year)
        print('Most Recent Birth Year:', most_recent_year)
        print('Most Common Birth Year:', most_common_year)
    else:
        print('\nBirth year data is not available for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    i = 0
    raw = input("Do you want to see the raw data? (yes or no) ").lower() 
    # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:
       if raw == 'no':
           break
       elif raw == 'yes':
           print(df[i:i+5])
           i += 5
           raw = input("Do you want to see more raw data? (yes or no) ").lower()
       else:
            raw = input("Invalid input. Please enter 'yes' or 'no': ").lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        while True:
            restart = input('\nWould you like to restart? Please enter yes or no.\n')
            if restart.lower() == 'yes':
                break
            elif restart.lower() == 'no':
                return
            else:
                print('Invalid input. Please enter either "yes" or "no".')


if __name__ == "__main__":
	main()
