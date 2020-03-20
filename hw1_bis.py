# zadanie 1
def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    """
    Returns confirmed infection cases for country 'Poland' given a date.
    Ex.
    >>> poland_cases_by_date(7, 3, 2020)
    5
    >>> poland_cases_by_date(11, 3)
    31
    :param year: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param day: Day of month to get the cases for as an integer indexed from 1
    :param month: Month to get the cases for as an integer indexed from 1
    :return: Number of cases on a given date as an integer
    """
    #case_date=[str(month) '/' str(day) '/' str(year)]#"3/15/20"
    case_date = str(month) + '/' + str(day) + '/' + str(year)[-2:]
    
    # Your code goes here (remove pass)
    no_cases = df.loc[df["Country/Region"]=="Poland", case_date].sum()
    return no_cases
    #pass
    
poland_cases_by_date(16, 3)#, 2020)



# zadanie 2

def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
    """
    Returns the top 5 infected countries given a date (confirmed cases).
    Ex.
    >>> top5_countries_by_date(27, 2, 2020)
    ['China', 'Korea, South', 'Cruise Ship', 'Italy', 'Iran']
    >>> top5_countries_by_date(12, 3)
    ['China', 'Italy', 'Iran', 'Korea, South', 'France']
    :param day: 4 digit integer representation of the year to get the countries for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: A list of strings with the names of the coutires
    """
    case_date = str(month) + '/' + str(day) + '/' + str(year)[-2:]
    
    formated_gdf = df.groupby(["Country/Region"]).sum().sort_values(by=case_date, ascending=False)[:5]
    formated_gdf.reset_index()
    
    return list(formated_gdf.index)
    # Your code goes here (remove pass)
    #pass
top5_countries_by_date(16, 3, 2020)

# zadanie 3
from datetime import date, timedelta

# Function name is wrong, read the pydoc
def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    """
    Returns the number of countries/regions where the infection count in a given day
    was NOT the same as the previous day.
    Ex.
    >>> no_new_cases_count(11, 2, 2020)
    35
    >>> no_new_cases_count(3, 3)
    57
    :param day: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: Number of countries/regions where the count has not changed in a day
    """
    
    if day>0 and month>0 and year>0:
        case_date = str(month) + '/' + str(day) + '/' + str(year)[-2:]
        previous_date = datetime.strptime(case_date, '%m/%d/%y') - timedelta(days=1)

        previous_date = previous_date.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0", "/")



        formated_gdf = df.groupby(["Country/Region"]).sum().sort_values(by=case_date, ascending=False)
        formated_gdf.reset_index()

        formated_gdf['diff'] = np.where(formated_gdf[previous_date]==formated_gdf[case_date], 0, 1)


        return formated_gdf['diff'].sum()
    else:
        return print('Zły format danych')
    # Your code goes here (remove pass)
    #pass
    
    no_new_cases_count(15, 3, 2020)
