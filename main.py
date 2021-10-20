
def show_menu():
    print('1.Citirea unei liste de numere float.')
    print('2.Afișarea părții întregi a tuturor numerelor din listă.')
    print('3.Să se afișeze toate numerele care aparțin unui interval deschis citit de la tastatură.')
    print('4.Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare.')
    print('5.Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din cuvinte care le descriu caracter cu caracter.')
    print('x.Inchide programul!')
#P1

def read_list() :
    floats_as_str = input('Dati o lista de float-uri separate prin spatiu: ')
    floats_as_list_of_str = floats_as_str.split(' ')
    floats = []
    for float_str in floats_as_list_of_str:
        floats.append(float(float_str))

    return floats

#P2

def parte_intreaga(lst):
    '''
    Ia partea intreaga a numerelor din lista initiala.
    :param lst: lista cu numere float
    :return: lista cu partile intregi ale numerelor
    '''

    list_intreg = []
    for num in lst:
        list_intreg.append(int(num))
    return list_intreg

def test_parte_intreaga():
    assert parte_intreaga([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert parte_intreaga([1, 11, 33]) == [1,11,33]
    assert parte_intreaga([]) == []

def rezolvare_parte_intreaga(lst):
    print(f'Lista cu partea intreaga din lista initiala: {lst} sunt: {parte_intreaga(lst)}')

#P3

def interval_deschis( lst , st, dr):
    '''
    Calculam numerele care apartin intervalului deschis dat de st d si dr din lst.
    :param lst: lista iniala de float-uri
    :param st: partea stanga a intervalului
    :param dr: partea dreapta a intervalului
    :return: intervalul cerut in lista interval
    '''
    interval = []

    for num in range(st+1,dr):
        num = float(num)
        interval.append(num)

    return interval


'''def test_interval_deschis():

    assert interval_deschis([1.5, -3.3, 8, 9.8, 3.2],-4, 5) == [1.5, -3.3, 3.2]
    assert interval_deschis([], -4, 5) == []
    assert interval_deschis([1.5, -3.3, 8, 9.8, 3.2], 11, 30) == []
'''
def rezolvare_interval_deschis(lst):
    st = str(input('Dati partea stanga a intervalului.'))
    dr = str(input('Dati partea dreapta a intervalului.'))
    rez = interval_deschis(lst,st,dr)
    print(f'Intervalul deschis cu numere de la tastatura din : {lst} este: { rez}')
#P4

def rez_ambele(lst):
    '''
    Functie care afiseaza numerele in care partea intreaga divide partea fractionara
    :return: lista care respecta regula
    '''
    result = []
    for elem in lst:
        str_elem = str(elem)
        if '.' in str_elem:
            decimals = str_elem.split('.')[1]
            numar = str_elem.split('.')[0]
            if   decimals % numar == 0:
                result.append(elem)
    return result

'''def test_ambele():
    assert rez_ambele([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]
    assert rez_ambele([]) == []
    assert rez_ambele([ 8, 9, 7]) == []
'''
def show_rez_ambele(lst):
    solutie = rez_ambele()
    print(f'Numerele din : {lst} care au partea fractionara care se divide cu partea intreaga este:{rez_ambele(lst)}')



def main():

    lst = []
    while True:
        show_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            lst = read_list()
        elif option == '2':
            rez = rezolvare_parte_intreaga(lst)
            print(rez)

        elif option == '3':
            rezo = rezolvare_interval_deschis(lst)
            print(rezo)

        elif option == '4':
            rez = rez_ambele(lst)
            print(rez)

        elif option == '5':
            pass

        elif option == 'x':
            break
        else:
            print('Optiune invalida, reincearca!')

if __name__ == '__main__':
    test_parte_intreaga()
    #test_interval_deschis()
    #test_ambele()
    main()

