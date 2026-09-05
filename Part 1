%%Lowpass filter removes frequency content, then only leaves the DC offset
%add gaussian random variable, (0,1) (can just use randn function)
%Determine probability that an error occurs, analytically and simulated
% How many times A/2 goes negative, or -A/2 goes positive

A_array=[0.01:0.01:10;]; %Magnitude of Signal from 0.01 to 10
W_array= randn(1,1000); %Magnitude of Gaussian Noise u=0 S.D.=1

P0 = 0.5; %Probabiliy of 0 as input
P1 = 0.5;%Probability of 1 as input


for i = 1:length(A_array)
    A=A_array(i);
    P_0_1 = 0; %P(0|1)
    P_1_0 = 0; %P(1|0)

    for j = 1:length(W_array)
    W=W_array(j);
        if(A/2<W)%(if W can make -A/2 positive)
          P_1_0=P_1_0+1;
        end
        if (-A/2>W)%(if W can make A/2 negative)
          P_0_1=P_0_1+1;
        end
    end
    %Perror=P(0|1)*P(1)+P(1|0)*P(0)
    Perror(i)=(P_0_1*P1+P_1_0*P0)./length(W_array);
    %disp(Perror);
end
%Theoretical P error for A values in array
Perror_theo = 1 - cdf('Normal', A_array/2,0,1);
figure(1)
subplot(121); plot(A_array, Perror,A_array, Perror_theo);
grid(1);
xlabel('Magnitude of Signal');
ylabel('P Error')
subplot(122); plot(A_array, Perror,A_array, Perror_theo);
grid(1)
xlabel('Magnitude of Signal');
ylabel('P Error')
xlim([4,6])
