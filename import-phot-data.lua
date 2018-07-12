local x, y = 216, 75
local r, g, b
local stage = 0
local ci = 0
for line in io.lines('disp56s-demo/rickroll-colors.txt') do
	currNum = tonumber(line)
	if stage == 0 then r = currNum end
	if stage == 1 then g = currNum end
	if stage == 2 then b = currNum end
	cid = sim.partID(x + ci, y)
	local cx, cy = x + ci, y
	if stage == 2 then
		sim.decoBox(cx, cy, cx, cy, r, g, b)
	end
	stage = stage + 1
	if stage == 3 then
		stage = 0
		ci = ci + 1
	end
end
local x, y = 330, 81
local stage = 0
local ci = 0
for line in io.lines('disp56s-demo/rickroll-data.txt') do
	fakeci = ci + 1
	if fakeci >= 500 then fakeci = 0 end
	local cx, cy = x + stage, y + fakeci
	if fakeci >= 250 then
		cx = x + 120 + stage
		cy = y + 250 - 1 - (fakeci-250)
	end
	cid = sim.partID(cx, cy)
	sim.partProperty(cid, sim.FIELD_CTYPE, bit.bor(tonumber(line), 0x20000000))
	stage = stage + 1
	if stage == 113 then
		stage = 0
		ci = ci + 1
	end
	if ci == 500 then break end
end
tpt.log('Done!')

