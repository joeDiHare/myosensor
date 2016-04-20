% %% generate accel and myo data
% x=round(0.5*[100 100 logspace(log10(100),0,1.1/0.05) logspace(0,log10(100),1.9/0.05-1) 100]+2*rand(1,61)-1);
% y=round(zeros(size(x))+2*rand(1,61)-1);
% z=round([0 logspace(0,log10(100),1.1/0.05) 100 logspace(log10(100),0,1.9/0.05-1) 0]+2*rand(1,61)-1);
% m=round(240*norma(smooth(x+2*z)));
% figure(1); cla;
% plot(1:length(z),m,'r',1:length(z),y,'g',1:length(z),x,1:length(z),z,'k');
% ylim([0 100]);
% 
% %% 50 ms frame, 50 samples (1kHz fs), for 3 s (60 reps)
% clc;
% for n=1:61
%     pause(50e-3);
%     time=round(now);
% %     for m=1:50
%         fprintf(1,'\n%d\t%d\t%d\t%d\t%d',time,m(n),x(n),y(n),z(n))
% %     end
% end


%% analise data
clear all; clc;
name = 'myodata-1461170687003.dat';
load(name)
eval(['myodata = ',strrep(name(1:end-4),'-','_')]);
t=myodata(:,1);
x=myodata(:,2);
y=myodata(:,3);
z=myodata(:,4);
m=myodata(:,5:end); m=m'; m=m(:)';

figure(10)
%display
for n=1:length(t)
    subplot(3,3,1); 
    for k=max(1,n-4):max(1,n-1), 
    bar(m(k),'FaceColor',0.1*(n-k)+[.5 .5 .5],'barwidth',.9+.1*(n-k)); hold on; end
    bar(m(n)); axis([0 2 0 255]); ylabel('strength'); hold off;
    subplot(3,3,[2 3]); 
    k=max(1,n-10):max(1,n-1);
    plot(x(k),z(k),'ow','markerfacecolor',[.5 .5 .5],'markersize',10); hold on; 
    plot(x(n),z(n),'o','color','k','markerfacecolor','k','markersize',10);
    axis([-20 65 0 105]);ylabel('z position');xlabel('x position'); hold off;
    subplot(3,3,[4:9]); 
    k=max(1,n-10):max(1,n-1);
    theta = atan2(z(n),x(n)); r=75; xseg = r.*cos(theta); zseg = r.*sin(theta);
    plot3([-50 0],[0 0],[100 0],'-k',[0 xseg],[0 0],[0 zseg],'-k','linewidth',10); hold on;
    plot3(x(k),y(k),z(k),'-.o','color',[.4 .4 .4],'markerfacecolor',[.5 .5 .5],'markersize',10); hold on; 
    plot3(x(n),y(n),z(n),'o','color','w','markerfacecolor','r','markersize',10); 
    view([-24.5 12]);hold off;
    ylabel('y position');xlabel('x position');zlabel('z position');
    axis([-20 80 -5 5 -20 100]);    
    grid on;
    pause(.1)
end
