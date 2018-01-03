import loadaerdat as ld
import spikes as spk
import sys

if __name__ == "__main__":
	#extract data
	print('Loading AEDAT file...')
	data = ld.loadaerdat('./mike1.aedat', 0, 'aedat', 1, 'DVS128')
	time = data[0]
	xaddr = data[1]
	yaddr = data[2]
	pol = spk.use_pm_polarity(data[3])
	
	#user defined vars
	#pixel of interest address
	myxaddr = 3
	myyaddr = 3
	#range around that pixel
	#note a big range can be expensive
	rng = 5
	
	#dummy data
	# xaddr = [1,2,3,4,3,3,6,3]
	# yaddr = [2,8,2,5,2,5,6,3]
	# pol = [0,0,1,0,0,1,1,0]
	# time = [0,1,2,3,4,5,6,7]
	
	input('Press any key to continue...')
	print('Starting spike tools...')
	considered_indexes = spk.keep_one_addr_with_rng(time=time, xaddr=xaddr, yaddr=yaddr, pol=pol, myxaddr=myxaddr, myyaddr=myyaddr, rng=rng)
	if considered_indexes == []:
		sys.exit('Error: no spikes were extracted for the specified address. Try another one.')
	print('Done extracting spikes')
	
	input('Press any key to continue...')
	spk.plot_polarity(time, pol, considered_indexes)