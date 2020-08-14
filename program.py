from helper import Helper
from carparser import CarParser
import os
import multiprocessing as mp
import glob


def process_page(page):
    print('processing page: ', page)
    soup = Helper.get_soup(page)
    ids_checkbox = soup.find_all('input', attrs={'type': 'checkbox', 'name': 'c'})
    csv_file = open("cars_page_%s.csv" % page, "w", encoding='utf-8-sig')

    for id_checkbox in ids_checkbox:
        car_id = id_checkbox.attrs['value']
        car = CarParser.parse_car(car_id)
        csv = car.get_csv()

        csv_file.write(csv)

    csv_file.close()


def merge_csv_files():
    all_filenames = [i for i in glob.glob('*.{}'.format('csv'))]
    with open('cars.csv', 'w', encoding='utf-8-sig') as outfile:
        for name in all_filenames:
            with open(name, encoding='utf-8-sig') as infile:
                outfile.write(infile.read())


def main():
    data_path = os.path.join(os.getcwd(), 'data')
    os.chdir(data_path)

    soup = Helper.get_soup(1)
    last_page = int(Helper.get_last_page(soup))
    print('Total pages: ', last_page)

    page_array = [(page,) for page in range(1, last_page + 1)]
    pool = mp.Pool(32)
    pool.starmap(process_page, page_array)
    print('Done scrapping data.')

    merge_csv_files()
    print('Done merging.')


if __name__== "__main__":
    main()