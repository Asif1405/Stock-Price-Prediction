#for voted classifier

clf.fit(x_train, y_train)

predictions = clf.predict(x_test)

rms=np.sqrt(np.mean(np.power((test-predictions),2)))
print(rms)

test_set["Prediction"] = predictions

#visualize output
train_set.Close.plot(figsize=(15,8), title= 'Closing Price', fontsize=14, label='train')
test_set.Close.plot(figsize=(15,8), title= 'Closing Price', fontsize=14, label='test')
test_set.Prediction.plot(figsize=(15,8), title= 'Predicted Closing Price', fontsize=14, label='predicted')
plt.xlabel("Datetime")
plt.ylabel("Closing Price")
plt.legend(loc='best')
plt.show()

#for NN
closing_price = model.predict(x_test)
closing_price = scaler.inverse_transform(closing_price)
closing_price = np.array(closing_price)

rms=np.sqrt(np.mean(np.power((test-closing_price),2)))
print(rms)
    
    
test_set["Prediction"] = closing_price

train_set.Close.plot(figsize=(15,8), title= 'Closing Price', fontsize=14, label='train')
test_set.Close.plot(figsize=(15,8), title= 'Closing Price', fontsize=14, label='test')
test_set.Prediction.plot(figsize=(15,8), title= 'Predicted Closing Price', fontsize=14, label='predicted')
plt.xlabel("Datetime")
plt.ylabel("Closing Price")
plt.legend(loc='best')
plt.show()
