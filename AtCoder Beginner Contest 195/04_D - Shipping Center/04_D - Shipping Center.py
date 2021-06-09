import sys
f = open('04_D - Shipping Center.txt', 'r')
sys.stdin = f

n, m, q = map(int, input().split(' '))
lags = []
for _ in range(n):
    w, v = map(int, input().split(' '))
    lags.append((w, v))
boxes = list(map(int, input().split(' ')))
lags = sorted(lags, key=lambda x: x[1])

for _ in range(q):
    rst = 0
    l, r = map(int, input().split(' '))
    tmp_boxes = boxes[:l - 1] + boxes[r:]
    tmp_boxes.sort()
    tmp_lags = lags.copy()
    for box in tmp_boxes:
        if len(tmp_lags) == 0:
            continue
        is_end = False
        for k, lag in enumerate(tmp_lags[::-1]):
            if is_end:
                continue
            if box >= lag[0]:
                rst += lag[1]
                tmp_lags.pop(len(tmp_lags) - k -1)
                is_end = True
    print(rst)