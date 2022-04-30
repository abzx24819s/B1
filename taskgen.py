import numpy
import sys
import ntlk
ntlk.download('stopwords')
from ntlk.tokenize import RegexTokenizer
from ntlk.corpus import stopwords
from keras.models import Sequential
from keras.layers import Dense,Dropout,LSTM
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
file=open('frankenstein-2.txt').read()
def token_words(input):
  input=input.lower()
  tokenizer=RegexpTokenizer(r'\w+')
  tokens=tokenizer.tokenize(input)
  filtered=filter(lambda token:token not in stopwords.words("english"),tokens)
  return"".join(filtered)
processed_inputs=tokenize_words(file)
chars=sorted(list(set(processed_input)))
char_to_num=dict((c,i) for i , c in enumerate(chars))
input_len=len(processed_inputs)
vocab_len=len(chars)
print("total no of chars :",input_len)
print("total vocab:",vocab_len)
seq_length=100
x_data=[]
y_data=[]
for i in range(0,input_len-seq_length,1):
   in_seq=processed_inputs[i:i+seq_length]
   out_seq=processed_inputs[i+ seq_length]
   x_data.append({char_to_num[char} for char in in_seq])
   y_data.append(char_to_num[out_seq])
n_patterns = len(x_data)
print("total patterns:",n_patterns)
X=numpy.reshape(x_data,(n_patterns,seq_length,1))
model=Sequential()
model.add(LSTM(256,input_shape=(X.shape[1],X.shape[2]),return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256,return_sequences=True))
model.add(Dropout(0.2))
model.add(LTSM(128))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1],activation="softmax"))
model.compile(loss="categorical_crossentropy",optimizer="adam")
filepath= "model_weights_saved.hdf5"
checkpoint=ModelCheckpoint(filepath,monitor="loss",verbpse=1,save_best_only=True,mode="min")
desired_callbacks=[checkpoint]
model.fit(X,y,epochs=4,batch_size=256,callbacks=desired_callbacks)
filepath= "model_weights_saved.hdf5"
model.load_weights(filename)
model.compile(loss="categorical_crossentropy",optimizer="adam")                 
num_to_char=dict((c,i) for i , c in enumerate(chars))
start=numpy.random.randit(0,len(x_data)-1)
pattern=x_data[start]
print("random seed:)
print("\"","".join([num_to_char[value] for value in pattern]),"\"")
for i in range(1000):
    x=numpy.reshape(patern,(1,len(pattern),1))
    x=x/float(vocab_len)
    prediction=model.predict(x,verbose=0)
    index=numpy.argmax(prediction)
    result=num_to_char[index]
    seq_in=[num_to_char] for value in pattern]
    sys.stdout.write(result)
    pattern.append(index)
    pattern=pattern[1:len(pattern)]
#-------------------
