"""
Clay Beal - Project 3 (Classes and CSV Files)
Date Created: 11/29/22

In association with Chance Carroll

This project takes a csv file from an Excel spreadsheet,
gets each column, does calculations on the values for
median, mean, standard deviation, min, and max, and puts
the values on a .docx file

I certify that this work was done in accordance with
GV academic honesty policies.

Fall, 2022
"""

from document_tools import DataFile, ReportGenerator


def main():
    """ Creates a file that makes an instance of a datafile and generates a report """
    datafile = DataFile("./data/vgsales.csv", "VGSales Report")
    datafile.set_description("This is a summary of video game sales information.")
    datafile.load()
    datafile.set_process([6, 7, 8, 9, 10, 11])
    generator = ReportGenerator(datafile)
    generator.generate('./data/output.docx')


if __name__ == '__main__':
    main()
