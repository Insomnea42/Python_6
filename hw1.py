#lambda

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Зачем выходить оттуда оттудабва, куда вернешься вернешьсяабв вечером таким же, каким ты был, тем бабволее более — изувеченным?'

def delete(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)
print(f'Текст для беты: {text}')
text = delete(text)
print(f'Отбечено: {text}')