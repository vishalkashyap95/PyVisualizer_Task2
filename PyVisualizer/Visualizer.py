from PyVisualizer.CommonUtilities import CommonUtilities
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# commonUtils = CommonUtilities()
# commonUtils.connectAndAutorizeToSeriveAccount()
# sheet1 = commonUtils.read_google_sheet(sGoogleSheetFileName="Copy_of_Greendeck_SE_Assignment_Task_2", sWorkSheetName="Sheet1")
# sheet1_data = sheet1.get_all_records()
# print(sheet1_data)

def barPlotSalesByYear(pandaDataFrame,xColName,yColName):
    """
    Helps in plotting a bar plot, Avg Sales by year on y axis and year on x axis
    :param dataFrame: accepts a pandas dataframe
    :param xColName: Column name to be plotted on x axis
    :param yColName: Column name to be plotted on y axis
    """
    pandaDataFrame['year'] = pandaDataFrame.timestamp.apply(lambda x: pd.Timestamp(x, unit='s').date().year)
    sns.barplot(x='year',y=yColName,data=pandaDataFrame)
    plt.ticklabel_format(style='plain',axis='y')
    plt.title("Avg Sales per year")
    plt.xlabel("Year(s)",fontsize=10)
    plt.ylabel("Average_sales",fontsize=10)
    plt.xticks(rotation=45)
    plt.show()

def barPlotSalesByMonth(dataFrame,xColName,yColName):
    """
    Helps in plotting a bar plot, Avg Sales by month on y axis and year on x axis
    :param dataFrame: accepts a pandas dataframe
    :param xColName: Column name to be plotted on x axis
    :param yColName: Column name to be plotted on y axis
    """
    dataFrame['month'] = dataFrame.timestamp.apply(lambda x: pd.Timestamp(x, unit='s').date().strftime("%B"))
    sns.barplot(x='month',y=yColName,data=dataFrame)
    plt.ticklabel_format(style='plain',axis='y')
    plt.title("Avg Sales by months")
    plt.xlabel("Months",fontsize=10)
    plt.ylabel("Average_sales",fontsize=10)
    plt.xticks(rotation=45)
    plt.show()

# barPlotSalesByYear(pd.DataFrame(sheet1_data),"timestamp","average_sales")
# barPlotSalesByMonth(pd.DataFrame(sheet1_data),"timestamp","average_sales")