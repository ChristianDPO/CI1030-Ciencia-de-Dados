#!/usr/bin/env python
"""
Script responsável para plotar um grafico de barras com a distribuição dos dados de um dataset
"""
import sys
import pandas
import matplotlib.pyplot as plt


def create_distribution_graph(csv_file, class_column_name):
    """
    Plots a barh graph with the class distribution of a csv file dataset

    :param str csv_file: path to the csv file
    :param class_column_name: the name of the csv column with the class labels
    """


    # Reads CSV file with data
    csv_data = pandas.read_csv(csv_file)

    #Create class name/label array and class count vectors
    class_names = csv_data[class_column_name].unique()
    class_counts = csv_data[class_column_name].value_counts()

    #Plot bar graph to show class sample distribution
    plt.xlabel('Classes')
    plt.ylabel('Number of samples') 
    plt.barh(class_names, class_counts, color='green')

    #Shows the exat class sample count on top of the bar 
    for index, value in enumerate(class_counts):
        plt.text(value, index,str(value))

    plt.show()


def do_main(csv_file, class_column_name):

    create_distribution_graph(
        csv_file=csv_file,
        class_column_name=class_column_name,
    )



if __name__ == '__main__':

    if len(sys.argv) < 3:
        exit("Usage: create_distribution_graph.py <csv_file> <class_column_name>")
    
    do_main(
        csv_file=sys.argv[1],
        class_column_name=sys.argv[2]
    )