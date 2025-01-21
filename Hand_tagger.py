import pandas as pd

def process_csv(file_path, max_zeros):
    df = pd.read_csv(file_path)

    if "Текст" not in df.columns:
        print("Ошибка: В файле отсутствует столбец 'текст'.")
        return

    processed_data = []  
    prev_text = None      
    zero_count = 0        

    for index, row in df.iterrows():
        text = row["Текст"]

        # Пропускаем повторяющийся текст
        if text == prev_text:
            continue

        # Вывод текста для пользователя
        print(f"Текст: {text}")

        while True:
            user_input = input("Введите 0 или 1: ")
            if user_input in ["0", "1"]:
                user_input = int(user_input)
                break
            print("Неверный ввод. Пожалуйста, введите 0 или 1.")

        processed_data.append({"text": text, "tag": user_input})

        prev_text = text

        if user_input == 0:
            zero_count += 1

        if zero_count >= max_zeros:
            print("Достигнуто максимальное количество строк со значением 0.")
            break

    result_df = pd.DataFrame(processed_data)
    print("Результаты:")
    print(result_df)

    return result_df

if __name__ == "__main__":
    file_path = input("Введите путь к CSV файлу: ")
    max_zeros = int(input("Введите максимальное количество строк со значением 0: "))
    result = process_csv(file_path, max_zeros)

    if result is not None:
        output_file = input("Введите путь для сохранения результата (например, output.csv): ")
        result.to_csv(output_file, sep=';', index=False)
        print(f"Результаты сохранены в файл {output_file}.")
