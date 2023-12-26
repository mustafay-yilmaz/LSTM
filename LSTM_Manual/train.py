#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
#Kendi Modüllerimiz
from lstm import sigmoid,tanh_activation,softmax,tanh_derivative # Aktivasyon Fonksiyonları
from lstm import initialize_parameters,initilaize_output_units #Parametreler
from lstm import lstm_cell,output_cell
from lstm import get_embeddings
from lstm import forward_propagation,backward_propagation
from lstm import cal_loss_accuracy
from lstm import calculate_output_cell_error
from lstm import calculate_single_lstm_cell_error
from lstm import calculate_output_cell_derivatives
from lstm import calculate_single_lstm_cell_derivatives
from lstm import calculate_output_cell_error
from lstm import update_parameters,update_embeddings
from lstm import initialize_V
from lstm import initialize_S
from lstm import train,predict,save_model
#%%
#path ="./data/lastname_tally.csv" # Türkçe isimler
path = "./data/tutunamayanlar.txt"
with open(path, "r", encoding="utf-8") as file:
    data = file.read()
#%%
import re
data = data.split(".")
data = [re.sub(r'[^\w\s]','',x) for x in data]
#data = pd.read_csv(path)

#get names from the dataset
#data['Name'] = data['Name']

#get first 10000 names
data = np.array(data[:10000]).reshape(-1,1)
#%%
#covert the names to lowee case
data = [x.lower() for x in data[:,0]]
data_n = []
for sentence in data:
    sentence = sentence.split(" ")
    #sentence = np.array(sentence).reshape(-1,1)
    data_n.append(sentence)
data = data_n
#%%
data = np.array(data).reshape(-1,1)

print("Data Shape = {}".format(data.shape))
print()
print("Lets see some names : ")
print(data[1:10])

#to store the transform data
transform_data = np.copy(data)

#find the max length name
max_length = 0
for index in range(len(data)):
    max_length = max(max_length,len(data[index,0]))

#make every name of max length by adding '.'
for index in range(len(data)):
    length = (max_length - len(data[index,0])) # O(k) ; Data Boyut
    string = ['.']*length
    transform_data[index,0] += string
    
print("Transformed Data")
print(transform_data[1:10])
#%%
#to store the vocabulary
vocab = list()
for name in transform_data[:,0]:
    vocab.extend(list(name))

vocab = set(vocab)
vocab_size = len(vocab)

initilaize_output_units(vocab_size=vocab_size,v=vocab)
#%%
print("Vocab size = {}".format(len(vocab)))
print("Vocab      = {}".format(vocab))

#map char to id and id to chars
char_id = dict()
id_char = dict()

for i,char in enumerate(vocab):
    char_id[char] = i
    id_char[i] = char

print('kirli-{}, 22-{}'.format(char_id['kirli'],id_char[22]))

# list of batches of size = 20
train_dataset = []

batch_size = 20

for i in range(len(transform_data)-batch_size+1):
    start = i*batch_size
    end = start+batch_size
    
    #batch data 
    batch_data = transform_data[start:end]
    
    if(len(batch_data)!=batch_size):
        break
        
    #convert each char of each name of batch data into one hot encoding
    char_list = []
    for k in range(len(batch_data[0][0])):#kelime uzunluğu 
        batch_dataset = np.zeros([batch_size,len(vocab)])
        for j in range(batch_size):
            name = batch_data[j][0]                            # T(n) ==> kelime uzunluğu x 20  
            char_index = char_id[name[k]]                     
            batch_dataset[j,char_index] = 1.0
     
        #store the ith char's one hot representation of each name in batch_data
        char_list.append(batch_dataset)
    
    #store each char's of every name in batch dataset into train_dataset
    train_dataset.append(char_list)


embeddings,parameters,J,P,A = train(train_dataset,iters=2500)
save_model(parameters=parameters,embeddings=embeddings,J=J,P=P,A=A,isim="trained_model",id_char=id_char,vocab_size=vocab_size) # Modeli kaydetme aşaması

avg_loss = list()
avg_acc = list()
avg_perp = list()
i = 0
while(i<len(J)):
    avg_loss.append(np.mean(J[i:i+30]))
    avg_acc.append(np.mean(A[i:i+30]))
    avg_perp.append(np.mean(P[i:i+30]))
    i += 30

plt.plot(list(range(len(avg_loss))),avg_loss)
plt.xlabel("x")
plt.ylabel("Loss (Avg of 30 batches)")
plt.title("Loss Graph")
plt.show()

plt.plot(list(range(len(avg_perp))),avg_perp)
plt.xlabel("x")
plt.ylabel("Perplexity (Avg of 30 batches)")
plt.title("Perplexity Graph")
plt.show()

plt.plot(list(range(len(avg_acc))),avg_acc)
plt.xlabel("x")
plt.ylabel("Accuracy (Avg of 30 batches)")
plt.title("Accuracy Graph")
plt.show()
