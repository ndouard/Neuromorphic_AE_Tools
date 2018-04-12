% csvwrite(filename,M)

function ExportToCSV(aedatStruct, filename)
fileID = fopen(filename,'wt');

% Grab polarity data from AEDAT struct
polarity = aedatStruct.data.polarity;
timeStamp = polarity.timeStamp;
y = polarity.y;
x = polarity.x;
polarity = polarity.polarity;
names = {'timeStamp', 'y', 'x', 'polarity'};

% Grab info from AEDAT struct
info = aedatStruct.info;
beginningOfDataPointer = info.beginningOfDataPointer;
fileFormat = info.fileFormat;
source = info.source;
deviceAddressSpace = info.deviceAddressSpace;
numEventsInFile = info.numEventsInFile;
firstTimeStamp = info.firstTimeStamp;
lastTimeStamp = info.lastTimeStamp;

%%%BEGIN WRITING HEADER LINES%%%
fprintf(fileID, '%s,', strcat('#beginningOfDataPointer=', int2str(beginningOfDataPointer)));
fprintf(fileID, '%s\n', '');

fprintf(fileID, '%s,', strcat('#fileFormat=', int2str(fileFormat)));
fprintf(fileID, '%s\n', '');

fprintf(fileID, '%s,', strcat('#source=', source));
fprintf(fileID, '%s\n', '');

fprintf(fileID, '%s,', strcat('#deviceAddressSpace=[', int2str(deviceAddressSpace(1)),...
                              '|', int2str(deviceAddressSpace(2)), ']'));
fprintf(fileID, '%s\n', '');

fprintf(fileID, '%s,', strcat('#numEventsInFile=', int2str(numEventsInFile)));
fprintf(fileID, '%s\n', '');

fprintf(fileID, '%s,', strcat('#firstTimeStamp=', int2str(firstTimeStamp)));
fprintf(fileID, '%s\n', '');

fprintf(fileID, '%s,', strcat('#lastTimeStamp=', int2str(lastTimeStamp)));
fprintf(fileID, '%s\n', '');
%%%END WRITING HEADER LINES%%%

% Write column headers to CSV
[rows, columns] = size(names);
for index = 1:rows    
    fprintf(fileID, '%s,', names{index,1:end-1});
    fprintf(fileID, '%s\n', names{index,end});
end 

fclose(fileID);

% Create dataix of AEDAT data where each element is its own column
data = [timeStamp, y, x, polarity];

% Append AEDAT data to CSV
dlmwrite(filename, data,'-append', 'delimiter', ',');

end