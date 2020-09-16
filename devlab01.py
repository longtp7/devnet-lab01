Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = dict[ ten='long']
SyntaxError: invalid syntax
>>> a= dict( ten = 'long', tuoi = 1, donvi='gnoc2')
>>> b= dict( ten = 'huan', tuoi = 1, donvi='gnoc2')
>>> c= dict( ten = 'minh', tuoi = 1, donvi='gnoc2')
>>> d=[a,b,c]
>>> print(a[ten])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(a[ten])
NameError: name 'ten' is not defined
>>> print (a[0])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print (a[0])
KeyError: 0
>>> print(a(ten))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(a(ten))
NameError: name 'ten' is not defined
>>> print(a['ten'])
long
>>> print(b['ten'])
huan
>>> print(c['ten'])
minh
>>> for x in d:
	print(x['ten'])
	print(x['tuoi'])
	print(x['donvi'])
	end

	
long
1
gnoc2
Traceback (most recent call last):
  File "<pyshell#16>", line 5, in <module>
    end
NameError: name 'end' is not defined
>>> for x in d:
	print(x['ten'])
	print(x['tuoi'])
	print(x['donvi'])

	
long
1
gnoc2
huan
1
gnoc2
minh
1
gnoc2
>>> 