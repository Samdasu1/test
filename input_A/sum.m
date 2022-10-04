clc, clear, close all

data_A = csvread('Demand_ResultData.csv');
data_B = data_A(:,7);
B = zeros(24,1);
for i = 1:24
    
    for j=1:4
        A = data_B(4*(i-1)+j);
        B(i) = A+B(i);
    end
end
        