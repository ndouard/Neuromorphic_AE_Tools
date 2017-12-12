import loadaerdat as ld
import spikes as spk

if __name__ == "__main__":
	print('Loading AEDAT file...')
	data = ld.loadaerdat('./mike1.aedat', 0, 'aedat', 1, 'DVS128')
	time = data[0]
	xaddr = data[1]
	yaddr = data[2]
	pol = spk.use_pm_polarity(data[3])
	print('Updated polarity style: ' + str(pol[0:10]))
	input('Press any key to continue...')
	print('Starting spike tools...')
	#spk.show_polarity(time, xaddr, yaddr, pol)
	common = spk.keep_one_addr_with_rng(time, xaddr, yaddr, pol, 34, 65, 10)
	print('Done extracting spikes')
	input('Press any key to continue...')
	spk.show_polarity(time, pol, common)
