load('TysenMelodies_20160420.mat');

FS=44100;
%WAVWRITE(Y,FS,WAVEFILE) 

nrec = size(s4c,1);

ngap= 44100-41013;
silence = zeros(ngap, 2);

melody_indx = [65,66,67,68,69];
melody_data = zeros(5, 41013, 2);
melody_data(1,:,:) = pm1;
melody_data(2,:,:) = pm2;
melody_data(3,:,:) = pm3;
melody_data(4,:,:) = pm4n;
melody_data(5,:,:) = pm5;


seq4c=[];
seq4v=[];
seq5c=[];
seq5v=[];

for irec = 1:nrec
    
    
    tmp4c = squeeze(melody_data(s4c(irec)-64,:,:));
    tmp4v = squeeze(melody_data(s4v(irec)-64,:,:));
    tmp5c = squeeze(melody_data(s5c(irec)-64,:,:));
    tmp5v = squeeze(melody_data(s5v(irec)-64,:,:));
    
    
    seq4c = [seq4c;tmp4c;silence];
    seq4v = [seq4v;tmp4v;silence];
    seq5c = [seq5c;tmp5c;silence];
    seq5v = [seq5v;tmp5v;silence];
end

wavwrite(seq4c, FS, 'seq4c_100sec.wav')
wavwrite(seq4v, FS, 'seq4v_100sec.wav')
wavwrite(seq5c, FS, 'seq5c_100sec.wav')
wavwrite(seq5v, FS, 'seq5v_100sec.wav')


group4c =find((s4c(2:end)-s4c(1:end-1))~=0);
group4v =find((s4v(2:end)-s4v(1:end-1))~=0);
group5c =find((s5c(2:end)-s5c(1:end-1))~=0);
group5v =find((s5v(2:end)-s5v(1:end-1))~=0);
