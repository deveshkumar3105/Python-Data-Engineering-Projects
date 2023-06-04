import pandas as pd
import DataSummarization


# Function to create DataFrame from a CSV File
def createDataframe():
    df = pd.read_csv("C:\\Users\\real robot\\Desktop\Datasets\\apple_products.csv")
    return df



if __name__=="__main__":

    # Create a DataFrame Function
    CreateDF = createDataframe()
    #print(CreateDF.head())


    # Data Summarization over different Columns
    SummaryDF = pd.DataFrame(columns=['ColName', 'Mean', 'MinCol', 'MaxCol', 'StdDev', 'Count'])
    colList = ['Sale Price','Mrp','Discount Percentage','Number Of Ratings','Number Of Reviews','Star Rating']
    for col in colList:
        mean = DataSummarization.mean(col, CreateDF)
        min = DataSummarization.min(col, CreateDF)
        max = DataSummarization.max(col, CreateDF)
        stdDev = DataSummarization.stdDev(col, CreateDF)
        count = len(CreateDF[col])

        SummaryDF = SummaryDF.append({
            'ColName':col,
            'Mean':mean,
            'MinCol':min,
            'MaxCol':max,
            'StdDev':stdDev,
            'Count':count
        }, ignore_index=True)
    print(SummaryDF)





