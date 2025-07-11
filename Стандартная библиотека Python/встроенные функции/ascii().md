#ПродвинутыйУровень #функция #ядроPython 

Функция `ascii()` возвращает строку, содержащую печатное представление объекта, где все не-ASCII символы заменены на escape-последовательности.

## 📌 Синтаксис и базовое использование

```python

ascii(object)
```

- **object** - любой Python объект (строка, число, список, словарь и т.д.)
    
- **Возвращает** строку, содержащую ASCII-представление объекта
    

### Простой пример

```python

print(ascii('hello'))  # 'hello'
print(ascii('привет'))  # '\u043f\u0440\u0438\u0432\u0435\u0442'
```

## 🔍 Как работает функция?

1. Для строк: заменяет все символы вне диапазона ASCII (0-127) на escape-последовательности:
    
    - `\x` для символов 0-255
        
    - `\u` для символов 256-65535
        
    - `\U` для символов выше 65536
        
2. Для других объектов: вызывает метод `__repr__()` объекта, затем экранирует не-ASCII символы в полученной строке
    

## 📊 Примеры использования

### Со строками

```python

# Английский текст (все символы ASCII)
print(ascii('Hello World!'))  # 'Hello World!'

# Русский текст
print(ascii('Привет'))  # '\u041f\u0440\u0438\u0432\u0435\u0442'

# Специальные символы
print(ascii(' café '))  # ' caf\xe9 '
```

### С другими типами данных

```python

# Список
print(ascii([1, 2, 'привет']))  # [1, 2, '\\u043f\\u0440\\u0438\\u0432\\u0435\\u0442']

# Словарь
print(ascii({'key': 'значение'}))  # {'key': '\\u0437\\u043d\\u0430\\u0447\\u0435\\u043d\\u0438\\u0435'}

# Числа (не меняются)
print(ascii(123))  # 123
```

## 🛠 Практическое применение

### 1. Безопасный вывод не-ASCII данных

```python

data = {'name': 'José', 'city': 'São Paulo'}
print(ascii(data))  # {'name': 'Jos\xe9', 'city': 'S\xe3o Paulo'}
```

### 2. Подготовка данных для систем, требующих ASCII

```python

text = "Café au lait"
safe_text = ascii(text)  # 'Caf\xe9 au lait'
```

### 3. Отладка с не-ASCII символами

```python

class Person:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Person({self.name!r})"


p = Person("Анна")
print(ascii(p))  # Person('\u0410\u043d\u043d\u0430')
```
## ⚠️ Важные особенности

1. **Отличие от repr()**:
    
    - `repr()` возвращает "сырое" представление объекта
        
    - `ascii()` дополнительно экранирует не-ASCII символы
        

```python

print(repr('é'))  # 'é'
print(ascii('é'))  # '\xe9'
```

2. **Для ASCII-символов** возвращает то же, что и `repr()`:
    
```python
s = 'hello'
print(repr(s) == ascii(s))  # True
```
    
- **Обратное преобразование**:  
    Можно использовать `eval()` или `ast.literal_eval()` для получения исходного объекта:
    
```python

escaped = ascii('привет')  # '\u043f\u0440\u0438\u0432\u0435\u0442'
original = eval(escaped)   # 'привет'
```
    

## 🔄 Сравнение с похожими функциями

|Функция|Возвращает|Обрабатывает не-ASCII|
|---|---|---|
|`str()`|читаемую строку|сохраняет как есть|
|`repr()`|представление для интерпретатора|сохраняет как есть|
|`ascii()`|представление для интерпретатора|экранирует|

## 🎯 Когда использовать?

1. При работе с системами, поддерживающими только ASCII
    
2. Для безопасного логирования данных с Unicode
    
3. При сериализации данных, которые должны быть ASCII-совместимыми
    
4. В отладочных целях для просмотра точного содержимого строк
    

## 💡 Продвинутое использование

### Кастомизация для своих классов

```python

class MyClass:
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"MyClass({self.value!r})"
        
    def __ascii__(self):
        return f"MyClass({ascii(self.value)})"

obj = MyClass(' café ')
print(ascii(obj))  # MyClass(' caf\xe9 ')
```

Функция `ascii()` — это важный инструмент для работы с Unicode в ASCII-совместимых средах, обеспечивающий безопасное представление любых данных.