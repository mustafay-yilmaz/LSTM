import config as c
import pickle
history=c.model.fit(c.predictors, c.label, epochs=100, verbose=5)

c.model.save("model9021.h5")

# History nesnesini bir dosyaya kaydetmek

with open('trainHistoryOld', 'wb') as handle:
    pickle.dump(history.history, handle)