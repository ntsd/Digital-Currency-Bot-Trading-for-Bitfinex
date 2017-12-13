import lstm
import time
import matplotlib.pyplot as plt
import csv

from keras.applications import imagenet_utils

def plot_results_multiple(predicted_data, true_data, prediction_len):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    # Pad the list of predictions to shift it in the graph to it's correct start
    for i, data in enumerate(predicted_data):
        padding = [None for p in range(i * prediction_len)]
        plt.plot(padding + data, label='Prediction')
        plt.legend()
    plt.show()

#Main Run Thread
if __name__=='__main__':
    global_start_time = time.time()
    epochs = 50
    seq_len = 50  # 50
    # how many time in windows example 1000 data 50 seq per window mean it will has 19 window for train and 1 window for test
    # seq mean how many data you look in past for predict next

    print('> Loading data... ')

    csv_path = '../Data/candles_to_btc/'

    csv_file_name = 'tOMGBTC_30m_08-07-17.csv'

    f = open(csv_path+csv_file_name, 'rb').read()
    data = []
    for row in f.decode().split('\n')[:-1]:
        # print("row:"+row)
        data.append(row.split(",")[2])
    X_train, y_train, X_test, y_test = lstm.load_data(data, seq_len, True)

    print('> Data Loaded. Compiling...')

    model = lstm.build_model([1, 50, 100, 1])  # add layers

    model.fit(
        X_train,
        y_train,
        batch_size=512,
        nb_epoch=epochs,
        validation_split=0.05)

    model_path = 'Models/'

    model_file_name = csv_file_name.replace(".csv", ".h")

    model.save(model_path+model_file_name)

    prediction_len = 10  # 50 what data to predict in the future
    # example if data every 30 minute you need to pre dict next 300 minute shoud be 10

    predictions = lstm.predict_sequences_multiple(model, X_test, seq_len, prediction_len)

    print('Training duration (s) : ', time.time() - global_start_time)
    plot_results_multiple(predictions, y_test, prediction_len*2 )