
class wordplay:
    l = ['jumbo' , 'lakshman' , 'surab' ,'shukla' , 'john' , 'nitasha' , 'fatima' , 'umar' , 'junaid' , 'talha' , 'sams' , 'manam']

    def word_with_length(self,length):
        lst = []
        for i in self.l:
           x = len(i)
           if x == length:
               lst.append(i)
        return lst


    def starts_with_s(self):
        lst = []
        for i in self.l:
            if i.startswith('s'):
                lst.append(i)
        return lst


    def ends_with_s(self):
        lst = []
        for i in self.l:
            if i.endswith('s'):
                lst.append(i)
        return lst


    def palindrom(self):
        lst = []
        for i in self.l:
            l = i[::-1]
            if i == l:
                lst.append(i)
        return lst







w = wordplay()
print('How many length of element')
l = int(input())
print(w.word_with_length(l))
print()
print('List Start With S Element')
print(w.starts_with_s())
print()
print('List End With S Element')
print(w.ends_with_s())
print()
print('List of Palindrom Word')
print(w.palindrom())