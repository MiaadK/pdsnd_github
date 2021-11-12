import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    The template was provided by Udacity
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
            city = str(input('Would you like to see data for Chicago, New York City, or Washington? ').lower())
            #city in CITY_DATA
            break
        except:
            print ('That\'s not a valid city! It should be Chicago, New York City, or Washington.')

    #filter_opts = ['month', 'day', 'both', 'none']
    while True:
        try:
            filter_opt = str(input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter. ').lower())
            #filter_opt in filter_opts
            break
        except:
            print ('That\'s not a valid answer!')

    #months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    if (filter_opt == 'month') or (filter_opt == 'both'):
    # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            try:
                month = str(input('which month? January, February, March, April, May, or June? ').lower())
                #month in months
                break
            except:
                print ('That\'s not a valid month!')
    else:
        month = 'all'

    if (filter_opt == 'day') or (filter_opt == 'both'):
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            try:
                day = str(input('which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? '))
                #(day >= 0) and (day <= 6) == True
                break
            except:
                print ('That\'s not a valid day!')
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0] - 1
    print("\nThe most popular month is " , months[popular_month])

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print("\nThe most popular day is " , popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\nThe most popular hour is " , popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_starts = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station is " , popular_starts)

    # TO DO: display most commonly used end station
    popular_ends = df['End Station'].mode()[0]
    print("\nThe most commonly used end station is " , popular_ends)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_ends'] = df['Start Station'] + ' & ' + df['End Station']
    popular_start_ends = df['start_ends'].mode()[0]
    print("\nThe most commonly used start & end station is " , popular_start_ends)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("\nThe total travel time in second is" , total_travel)


    # TO DO: display mean travel time
    max_travel = df['Trip Duration'].max()
    print("\nThe maximum travel time in second is" , max_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\Counts of user types are: ' , user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print('\Counts of user genders are: ' , user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]

        print('\The earliest year of birth is: ', earliest)
        print('\The most recent year of birth is: ', most_recent)
        print('\The most common year of birth is: ', most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        row = 0
        see_data = input('\nWould you like to see the firts five rows of data? Enter yes or no.\n')
        if see_data.lower() == 'yes':
            while True:
                for i in range(5):
                    print(df.iloc[[int(row + i)]])
                row += 5
                see_data = input('\nWould you like to see more data? Enter yes or no.\n')
                if see_data.lower() != 'yes':
                    break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
