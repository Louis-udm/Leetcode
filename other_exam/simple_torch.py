import torch
import torch.nn.functional as F

def logistic_regression_training(arr):
  # arr=[x,y,a,b]
  arr=[float(i) for i in arr]
  a = torch.tensor(arr[2], requires_grad=True)
  b = torch.tensor(arr[3], requires_grad=True)
  x = torch.tensor(arr[0])  # Example input data
  y = torch.tensor(arr[1])  # Example target values

  learning_rate = 1.0
  criterion=torch.nn.BCEWithLogitsLoss()
  # criterion=torch.nn.BCELoss()

  y_pred = 1.0 / (1.0 + torch.exp(-a * x - b))
  # y_pred = torch.sigmoid(y_pred)
  # loss = criterion(y_pred, y)
  loss = F.mse_loss(y_pred, y)
  # loss = y-y_pred
  loss.backward()
  with torch.no_grad():
      a_update=a- learning_rate * a.grad
      b_update=b- learning_rate * b.grad


  # epoch = 10
  # for _ in range(epoch):
  #     y_pred = 1.0 / (1.0 + torch.exp(-a * x - b))
  #     loss = F.mse_loss(y_pred, y)
  #     loss.backward()
  #     with torch.no_grad():
  #         a -= learning_rate * a.grad
  #         b -= learning_rate * b.grad

  #     a.grad.zero_()
  #     b.grad.zero_()

  return [a_update.item(), b_update.item()]

print(logistic_regression_training([1,1,1,1]))
print(logistic_regression_training([2.2,0.0,5.1,5.7]))