## purchaseOrder : 15

max gas:  36979
```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 15.sol:purchaseOrder:
INFO:symExec:   ============ Results ===========
INFO:symExec:     EVM Code Coverage:                     72.5%
INFO:symExec:     Integer Underflow:                     True
INFO:symExec:     Integer Overflow:                      False
INFO:symExec:     Parity Multisig Bug 2:                 False
INFO:symExec:     Callstack Depth Attack Vulnerability:  False
INFO:symExec:     Transaction-Ordering Dependence (TOD): False
INFO:symExec:     Timestamp Dependency:                  False
INFO:symExec:     Re-Entrancy Vulnerability:             False
INFO:symExec:15.sol:37:6: Warning: Integer Underflow.
     string public productNumber
INFO:symExec:   ====== Analysis Completed ======
```

## Ownable : 15
max gas:  7090

```
INFO:root:contract 15.sol:Ownable:
INFO:symExec:   ============ Results ===========
INFO:symExec:     EVM Code Coverage:                     99.6%
INFO:symExec:     Integer Underflow:                     False
INFO:symExec:     Integer Overflow:                      False
INFO:symExec:     Parity Multisig Bug 2:                 False
INFO:symExec:     Callstack Depth Attack Vulnerability:  False
INFO:symExec:     Transaction-Ordering Dependence (TOD): False
INFO:symExec:     Timestamp Dependency:                  False
INFO:symExec:     Re-Entrancy Vulnerability:             False
INFO:symExec:   ====== Analysis Completed ======
```

## Bank : 14
max gas:  6652
```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract bank.sol:Bank:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 98.8%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 True
INFO:symExec:bank.sol:14:37: Warning: Integer Overflow.
         userBalances[msg.sender] = userBalances[msg.sender] + msg.value
Integer Overflow occurs if:
    userBalances[msg.sender] = 1
INFO:symExec:bank.sol:20:14: Warning: Re-Entrancy Vulnerability.
         if (msg.sender.call.value(amountToWithdraw)()
INFO:symExec:	====== Analysis Completed ======
```

<br><br><br>
<br><br><br>
## BankAttacker : 14

max gas:  5818

```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract attk.sol:BankAttacker:
INFO:symExec:   ============ Results ===========
INFO:symExec:     EVM Code Coverage:                     97.6%
INFO:symExec:     Integer Underflow:                     False
INFO:symExec:     Integer Overflow:                      False
INFO:symExec:     Parity Multisig Bug 2:                 False
INFO:symExec:     Callstack Depth Attack Vulnerability:  False
INFO:symExec:     Transaction-Ordering Dependence (TOD): True
INFO:symExec:     Timestamp Dependency:                  False
INFO:symExec:     Re-Entrancy Vulnerability:             False
INFO:symExec:Flow1
attk.sol:39:18: Warning: Transaction-Ordering Dependency.
         require(msg.sender.send(address(this).balance)
Flow2
attk.sol:23:13: Warning: Transaction-Ordering Dependency.
         if(bankAddress.call.value(msg.value).gas(20764)(bytes4(keccak256("addToBalance()")))
INFO:symExec:   ====== Analysis Completed ======
```

## Exchange : 17

max gas:  5439

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 17/17.sol:Exchange:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 99.1%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 False
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:	====== Analysis Completed ======
```

## Owned : 16
max gas:  12289
```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract owned.sol:Owned:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 99.7%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 False
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:	====== Analysis Completed ======
```

## MoonCatRescue : 1

max gas:  43108
```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 1.sol:MoonCatRescue:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 13.9%
INFO:symExec:	  Integer Underflow: 			 True
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:1.sol:12:3: Warning: Integer Underflow.
  string public name = "MoonCats"
1.sol:189:34: Warning: Integer Underflow.
    searchSeed = block.blockhash(block.number - 1
Integer Underflow occurs if:
    owner = 0
1.sol:315:5: Warning: Integer Underflow.
    balanceOf[from]--
INFO:symExec:1.sol:98:5: Warning: Integer Overflow.
    adoptionOffers[catId] = AdoptionOffer(true, catId, msg.sender, price, 0x0)
Integer Overflow occurs if:
    price = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    catOwners[catId] = 0
1.sol:118:13: Warning: Integer Overflow.
    require(offer.onlyOfferTo
1.sol:120:20: Warning: Integer Overflow.
    if(msg.value > offer.price
1.sol:123:54: Warning: Integer Overflow.
    transferCat(catId, catOwners[catId], msg.sender, offer.price
1.sol:316:5: Warning: Integer Overflow.
    balanceOf[to]++
Integer Overflow occurs if:
    balanceOf[to] = 115792089237316195423570985008687907853269984665640564039457584007913129639935
1.sol:317:5: Warning: Integer Overflow.
    adoptionOffers[catId] = AdoptionOffer(false, catId, 0x0, 0, 0x0)
INFO:symExec:	====== Analysis Completed ======
```

## CryptoPunksMarket : 2

max gas:  79363

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 2/2.sol:CryptoPunksMarket:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 83.2%
INFO:symExec:	  Integer Underflow: 			 True
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): True
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:2/2.sol:10:5: Warning: Integer Underflow.
    string public name
2/2.sol:221:10: Warning: Integer Underflow.
        balanceOf[seller]--;
2/2.sol:5:5: Warning: Integer Underflow.
    string public imageHash = "ac39af4793119ee46bbff351d8cb6b5f23da60222126add4268e261199a2921b"
2/2.sol:9:5: Warning: Integer Underflow.
    string public standard = 'CryptoPunks'
2/2.sol:168:10: Warning: Integer Underflow.
        balanceOf[seller]--;
2/2.sol:118:10: Warning: Integer Underflow.
        balanceOf[msg.sender]--;
2/2.sol:11:5: Warning: Integer Underflow.
    string public symbol
2/2.sol:77:18: Warning: Integer Underflow.
                punksRemainingToAssign--;
2/2.sol:75:18: Warning: Integer Underflow.
                balanceOf[punkIndexToAddress[punkIndex]]--;
INFO:symExec:2/2.sol:42:5: Warning: Integer Overflow.
    mapping (uint => Offer) public punksOfferedForSale
2/2.sol:203:14: Warning: Integer Overflow.
        if (existing.value
2/2.sol:207:10: Warning: Integer Overflow.
        punkBids[punkIndex] = Bid(true, punkIndex, msg.sender, msg.value);
2/2.sol:205:53: Warning: Integer Overflow.
            pendingWithdrawals[existing.bidder] += existing.value;
2/2.sol:205:33: Warning: Integer Overflow.
            pendingWithdrawals[existing.bidder]
2/2.sol:205:14: Warning: Integer Overflow.
            pendingWithdrawals[existing.bidder] += existing.value;
2/2.sol:220:42: Warning: Integer Overflow.
        punkIndexToAddress[punkIndex] = bid.bidder;
2/2.sol:222:20: Warning: Integer Overflow.
        balanceOf[bid.bidder]
2/2.sol:222:10: Warning: Integer Overflow.
        balanceOf[bid.bidder]++;
2/2.sol:223:27: Warning: Integer Overflow.
        Transfer(seller, bid.bidder,
2/2.sol:225:67: Warning: Integer Overflow.
        punksOfferedForSale[punkIndex] = Offer(false, punkIndex, bid.bidder,
2/2.sol:225:10: Warning: Integer Overflow.
        punksOfferedForSale[punkIndex] = Offer(false, punkIndex, bid.bidder, 0, 0x0);
2/2.sol:226:24: Warning: Integer Overflow.
        uint amount = bid.value;
2/2.sol:227:10: Warning: Integer Overflow.
        punkBids[punkIndex] = Bid(false, punkIndex, 0x0, 0);
2/2.sol:228:10: Warning: Integer Overflow.
        pendingWithdrawals[seller] += amount;
2/2.sol:229:51: Warning: Integer Overflow.
        PunkBought(punkIndex, bid.value, seller, bid.bidder)
2/2.sol:229:32: Warning: Integer Overflow.
        PunkBought(punkIndex, bid.value,
2/2.sol:85:6: Warning: Integer Overflow.
    function setInitialOwners(address[] addresses, uint[] indices) {
    ^
Spanning multiple lines.
2/2.sol:45:5: Warning: Integer Overflow.
    mapping (uint => Bid) public punkBids
2/2.sol:165:27: Warning: Integer Overflow.
        address seller = offer.seller;
2/2.sol:169:10: Warning: Integer Overflow.
        balanceOf[msg.sender]++;
2/2.sol:136:10: Warning: Integer Overflow.
        punksOfferedForSale[punkIndex] = Offer(false, punkIndex, msg.sender, 0, 0x0);
2/2.sol:173:10: Warning: Integer Overflow.
        pendingWithdrawals[seller] += msg.value;
2/2.sol:179:14: Warning: Integer Overflow.
        if (bid.bidder
2/2.sol:181:48: Warning: Integer Overflow.
            pendingWithdrawals[msg.sender] += bid.value;
2/2.sol:181:14: Warning: Integer Overflow.
            pendingWithdrawals[msg.sender] += bid.value;
2/2.sol:182:14: Warning: Integer Overflow.
            punkBids[punkIndex] = Bid(false, punkIndex, 0x0, 0);
2/2.sol:119:10: Warning: Integer Overflow.
        balanceOf[to]++;
2/2.sol:125:14: Warning: Integer Overflow.
        if (bid.bidder
2/2.sol:127:40: Warning: Integer Overflow.
            pendingWithdrawals[to] += bid.value;
2/2.sol:127:14: Warning: Integer Overflow.
            pendingWithdrawals[to] += bid.value;
2/2.sol:128:14: Warning: Integer Overflow.
            punkBids[punkIndex] = Bid(false, punkIndex, 0x0, 0);
2/2.sol:80:14: Warning: Integer Overflow.
            balanceOf[to]++;
2/2.sol:152:10: Warning: Integer Overflow.
        punksOfferedForSale[punkIndex] = Offer(true, punkIndex, msg.sender, minSalePriceInWei, toAddress);
2/2.sol:144:10: Warning: Integer Overflow.
        punksOfferedForSale[punkIndex] = Offer(true, punkIndex, msg.sender, minSalePriceInWei, 0x0);
2/2.sol:104:10: Warning: Integer Overflow.
        balanceOf[msg.sender]++;
INFO:symExec:Flow1
2/2.sol:192:10: Warning: Transaction-Ordering Dependency.
        msg.sender.transfer(amount);
Flow2
2/2.sol:243:10: Warning: Transaction-Ordering Dependency.
        msg.sender.transfer(amount);
INFO:symExec:	====== Analysis Completed ======
```

## library SafeMathLibExt : 3

max gas:  356

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 3/3.sol:SafeMathLibExt:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 90.6%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:3/3.sol:41:14: Warning: Integer Overflow.
    uint c = a + b
Integer Overflow occurs if:
    a = 1
    b = 115792089237316195423570985008687907853269984665640564039457584007913129639935
INFO:symExec:	====== Analysis Completed ======
```

## PromissoryToken : 4

max gas:  11727

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 4/4.sol:PromissoryToken:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 56.9%
INFO:symExec:	  Integer Underflow: 			 True
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:4/4.sol:376:9: Warning: Integer Underflow.
        return (
        ^
Spanning multiple lines.
Integer Underflow occurs if:
    _withdrawalID = 0
    return (
            withdrawals[_withdrawalID].Amount,
            withdrawals[_withdrawalID].approved,
            withdrawals[_withdrawalID].reason,
            withdrawals[_withdrawalID].backerApprovals,
            withdrawals[_withdrawalID].totalStake,
            withdrawals[_withdrawalID].destination) = 1
    withdrawals[_withdrawalID] = 1
4/4.sol:169:69: Warning: Integer Underflow.
        backers[_backer].push(backerData(_tokenPrice, _tokenAmount, sha3(_privatePhrase, _backer)
Integer Underflow occurs if:
    _tokenAmount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backers[_backer].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    numOfBackers = 0
    earlyBackerList.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    promissoryUnits = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    claimedUnits = 0
    prepaidUnits = 0
    _tokenPrice = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    founder = 0
    claimedPrepaidUnits = 0
4/4.sol:79:5: Warning: Integer Underflow.
    withdrawalData[] public withdrawals
4/4.sol:196:55: Warning: Integer Underflow.
           backers[msg.sender][_index].privateHash == sha3( _privatePhrase, msg.sender)
Integer Underflow occurs if:
    backers[msg.sender][_index].prepaid = 255
    _index = 0
    earlyBackerList.length = 0
    backers[msg.sender][_index] = 1
    numOfBackers = 0
    _boughtTokensPrice = 0
    backers[msg.sender][_index].tokenPrice = 0
    _tokenAmount = 0
    backers[msg.sender][_index].tokenAmount = 0
INFO:symExec:4/4.sol:377:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID]
Integer Overflow occurs if:
    _withdrawalID = 19298681539552699258185503286070253854997628854965648752103403391503744456022
    withdrawals[_withdrawalID] = 19298681539552699258185503286070253854997628854965648752103403391503744456023
4/4.sol:378:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID]
Integer Overflow occurs if:
    _withdrawalID = 19298681539552699258185503286070253854997628854965648752103403391503744456022
    withdrawals[_withdrawalID] = 19298681539552699258185503286070253854997628854965648752103403391503744456023
4/4.sol:378:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID].approved
Integer Overflow occurs if:
    _withdrawalID = 0
    withdrawals[_withdrawalID] = 1
4/4.sol:379:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID]
Integer Overflow occurs if:
    _withdrawalID = 19298681539552699258185503286070253854997628854965648752103403391503744456022
    withdrawals[_withdrawalID] = 19298681539552699258185503286070253854997628854965648752103403391503744456023
4/4.sol:379:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID].reason
Integer Overflow occurs if:
    _withdrawalID = 0
    withdrawals[_withdrawalID] = 1
4/4.sol:380:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID]
Integer Overflow occurs if:
    _withdrawalID = 19298681539552699258185503286070253854997628854965648752103403391503744456022
    withdrawals[_withdrawalID] = 19298681539552699258185503286070253854997628854965648752103403391503744456023
4/4.sol:380:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID].backerApprovals
Integer Overflow occurs if:
    _withdrawalID = 0
    withdrawals[_withdrawalID] = 1
4/4.sol:381:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID]
Integer Overflow occurs if:
    _withdrawalID = 19298681539552699258185503286070253854997628854965648752103403391503744456022
    withdrawals[_withdrawalID] = 19298681539552699258185503286070253854997628854965648752103403391503744456023
4/4.sol:381:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID].totalStake
Integer Overflow occurs if:
    _withdrawalID = 0
    withdrawals[_withdrawalID] = 1
4/4.sol:382:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID]
Integer Overflow occurs if:
    _withdrawalID = 19298681539552699258185503286070253854997628854965648752103403391503744456022
    withdrawals[_withdrawalID] = 19298681539552699258185503286070253854997628854965648752103403391503744456023
4/4.sol:382:13: Warning: Integer Overflow.
            withdrawals[_withdrawalID].destination
Integer Overflow occurs if:
    _withdrawalID = 0
    withdrawals[_withdrawalID] = 1
4/4.sol:65:5: Warning: Integer Overflow.
    address[] public backersAddresses
4/4.sol:320:29: Warning: Integer Overflow.
        uint withdrawalID = withdrawals.length++
Integer Overflow occurs if:
    withdrawals.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    _totalAmount = 0
    founder = 0
4/4.sol:169:69: Warning: Integer Overflow.
        backers[_backer].push(backerData(_tokenPrice, _tokenAmount, sha3(_privatePhrase, _backer)
Integer Overflow occurs if:
    _tokenAmount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backers[_backer].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    numOfBackers = 0
    earlyBackerList.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    promissoryUnits = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    claimedUnits = 0
    prepaidUnits = 0
    _tokenPrice = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    founder = 0
    claimedPrepaidUnits = 0
4/4.sol:1:24: Warning: Integer Overflow.

Integer Overflow occurs if:
    backers[_backer].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    _tokenAmount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    numOfBackers = 0
    earlyBackerList.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    promissoryUnits = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    claimedUnits = 0
    prepaidUnits = 0
    _tokenPrice = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    founder = 0
    claimedPrepaidUnits = 0
4/4.sol:253:13: Warning: Integer Overflow.
            backers[_backerAddress][index]
Integer Overflow occurs if:
    index = 115792089237316195423570985008687907853269984665640564039457575000713874898943
    backers[_backerAddress][index] = 115792089237316195423570985008687907853269984665640564039457575000713874898944
4/4.sol:254:13: Warning: Integer Overflow.
            backers[_backerAddress][index]
Integer Overflow occurs if:
    index = 115792089237316195423570985008687907853269984665640564039457575000713874898943
    backers[_backerAddress][index] = 115792089237316195423570985008687907853269984665640564039457575000713874898944
4/4.sol:254:13: Warning: Integer Overflow.
            backers[_backerAddress][index].tokenAmount
Integer Overflow occurs if:
    index = 0
    backers[_backerAddress][index] = 1
4/4.sol:255:13: Warning: Integer Overflow.
            backers[_backerAddress][index]
Integer Overflow occurs if:
    index = 115792089237316195423570985008687907853269984665640564039457575000713874898943
    backers[_backerAddress][index] = 115792089237316195423570985008687907853269984665640564039457575000713874898944
4/4.sol:255:13: Warning: Integer Overflow.
            backers[_backerAddress][index].privateHash
Integer Overflow occurs if:
    index = 0
    backers[_backerAddress][index] = 1
4/4.sol:256:13: Warning: Integer Overflow.
            backers[_backerAddress][index]
Integer Overflow occurs if:
    index = 115792089237316195423570985008687907853269984665640564039457575000713874898943
    backers[_backerAddress][index] = 115792089237316195423570985008687907853269984665640564039457575000713874898944
4/4.sol:256:13: Warning: Integer Overflow.
            backers[_backerAddress][index].prepaid
Integer Overflow occurs if:
    index = 0
    backers[_backerAddress][index] = 1
4/4.sol:257:13: Warning: Integer Overflow.
            backers[_backerAddress][index]
Integer Overflow occurs if:
    index = 115792089237316195423570985008687907853269984665640564039457575000713874898943
    backers[_backerAddress][index] = 115792089237316195423570985008687907853269984665640564039457575000713874898944
4/4.sol:257:13: Warning: Integer Overflow.
            backers[_backerAddress][index].claimed
Integer Overflow occurs if:
    index = 0
    backers[_backerAddress][index] = 1
4/4.sol:79:5: Warning: Integer Overflow.
    withdrawalData[] public withdrawals
4/4.sol:66:5: Warning: Integer Overflow.
    mapping(address => backerData[]) public backers
4/4.sol:346:17: Warning: Integer Overflow.
            if (backers[_backerAddr][i].claimed
Integer Overflow occurs if:
    backers[_backerAddr].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backersRedeemed[_backerAddr] = 0
4/4.sol:349:28: Warning: Integer Overflow.
            totalTokens += backers[_backerAddr][i].tokenAmount
Integer Overflow occurs if:
    backers[_backerAddr][i].claimed = 65280
    backers[_backerAddr].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backersRedeemed[_backerAddr] = 0
4/4.sol:346:17: Warning: Integer Overflow.
            if (backers[_backerAddr][i]
Integer Overflow occurs if:
    backers[_backerAddr].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backers[_backerAddr][i].claimed = 65280
    backersRedeemed[_backerAddr] = 0
4/4.sol:349:28: Warning: Integer Overflow.
            totalTokens += backers[_backerAddr][i]
Integer Overflow occurs if:
    backers[_backerAddr].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backers[_backerAddr][i].claimed = 65280
    backers[_backerAddr][i].claimed = 65280
    backersRedeemed[_backerAddr] = 0
4/4.sol:349:13: Warning: Integer Overflow.
            totalTokens += backers[_backerAddr][i].tokenAmount
Integer Overflow occurs if:
    backers[_backerAddr].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backers[_backerAddr][i].tokenAmount = 1
    backers[_backerAddr][i].tokenAmount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backers[_backerAddr][i].claimed = 65280
    backers[_backerAddr][i].claimed = 65280
    backersRedeemed[_backerAddr] = 0
4/4.sol:42:5: Warning: Integer Overflow.
    address [] public previousFounders
4/4.sol:274:28: Warning: Integer Overflow.
            backerStake += backers[msg.sender][i].tokenAmount
Integer Overflow occurs if:
    _withdrawalID = 0
    withdrawalsVotes[msg.sender][_withdrawalID] = 0
    withdrawals[_withdrawalID].spent = 0
    withdrawals[_withdrawalID] = 1
    backers[msg.sender].length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
4/4.sol:276:9: Warning: Integer Overflow.
        withdrawals[_withdrawalID]
Integer Overflow occurs if:
    backers[msg.sender].length = 1
    _withdrawalID = 19298681539552699258185503286070253854997628854965648752103403391503744456022
    withdrawalsVotes[msg.sender][_withdrawalID] = 0
    withdrawals[_withdrawalID].spent = 0
    withdrawals[_withdrawalID] = 19298681539552699258185503286070253854997628854965648752103403391503744456023
4/4.sol:276:9: Warning: Integer Overflow.
        withdrawals[_withdrawalID].backerApprovals
Integer Overflow occurs if:
    backers[msg.sender].length = 1
    _withdrawalID = 0
    withdrawalsVotes[msg.sender][_withdrawalID] = 0
    withdrawals[_withdrawalID].spent = 0
    withdrawals[_withdrawalID] = 1
4/4.sol:274:28: Warning: Integer Overflow.
            backerStake += backers[msg.sender][i]
Integer Overflow occurs if:
    backers[msg.sender].length = 115792089236894946256896756261896235742535302936364983657855387562895885729791
    _withdrawalID = 0
    withdrawalsVotes[msg.sender][_withdrawalID] = 0
    withdrawals[_withdrawalID].spent = 0
    withdrawals[_withdrawalID] = 1
4/4.sol:274:13: Warning: Integer Overflow.
            backerStake += backers[msg.sender][i].tokenAmount
Integer Overflow occurs if:
    backers[msg.sender].length = 115792089237312904414456342596603597914904869964630598567726316848186432421887
    _withdrawalID = 0
    backers[msg.sender][i].tokenAmount = 1
    backers[msg.sender][i].tokenAmount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    withdrawalsVotes[msg.sender][_withdrawalID] = 0
    withdrawals[_withdrawalID].spent = 0
    withdrawals[_withdrawalID] = 1
4/4.sol:64:5: Warning: Integer Overflow.
    address[] public earlyBackerList
4/4.sol:199:13: Warning: Integer Overflow.
            backers[msg.sender][_index]
Integer Overflow occurs if:
    _index = 115792089237303031387112415360350668099809525861600547410027604696471978377215
    backers[msg.sender][_index].prepaid = 255
    earlyBackerList.length = 0
    backers[msg.sender][_index] = 115792089237303031387112415360350668099809525861600547410027604696471978377216
    numOfBackers = 0
    _backerRank = 0
    backers[msg.sender][_index].backerRank = 0
    backers[msg.sender][_index].privateHash = 0
    _boughtTokensPrice = 0
    backers[msg.sender][_index].tokenPrice = 0
    _tokenAmount = 0
    backers[msg.sender][_index].tokenAmount = 0
4/4.sol:199:13: Warning: Integer Overflow.
            backers[msg.sender][_index].claimed
Integer Overflow occurs if:
    backers[msg.sender][_index].prepaid = 255
    _index = 0
    earlyBackerList.length = 0
    backers[msg.sender][_index] = 1
    numOfBackers = 0
    _backerRank = 0
    backers[msg.sender][_index].backerRank = 0
    backers[msg.sender][_index].privateHash = 0
    _boughtTokensPrice = 0
    backers[msg.sender][_index].tokenPrice = 0
    _tokenAmount = 0
    backers[msg.sender][_index].tokenAmount = 0
4/4.sol:200:13: Warning: Integer Overflow.
            claimedPrepaidUnits += _tokenAmount
Integer Overflow occurs if:
    backers[msg.sender][_index].prepaid = 255
    _index = 0
    claimedPrepaidUnits = 1
    earlyBackerList.length = 0
    _tokenAmount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    backers[msg.sender][_index] = 1
    numOfBackers = 0
    _backerRank = 0
    backers[msg.sender][_index].backerRank = 0
    backers[msg.sender][_index].privateHash = 0
    _boughtTokensPrice = 0
    backers[msg.sender][_index].tokenPrice = 0
    backers[msg.sender][_index].tokenAmount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
4/4.sol:202:13: Warning: Integer Overflow.
            PrepaidTokensClaimedEvent(msg.sender, _index, _boughtTokensPrice, _tokenAmount)
Integer Overflow occurs if:
    backers[msg.sender][_index].prepaid = 255
    _index = 0
    earlyBackerList.length = 0
    backers[msg.sender][_index] = 1
    numOfBackers = 0
    _backerRank = 0
    backers[msg.sender][_index].backerRank = 0
    backers[msg.sender][_index].privateHash = 0
    _boughtTokensPrice = 0
    backers[msg.sender][_index].tokenPrice = 0
    _tokenAmount = 0
    backers[msg.sender][_index].tokenAmount = 0
INFO:symExec:	====== Analysis Completed ======
```
## DigiPulse : 5

max gas:  16222

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 5/5.sol:DigiPulse:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 74.2%
INFO:symExec:	  Integer Underflow: 			 True
INFO:symExec:	  Integer Overflow: 			 False
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): True
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:5/5.sol:143:10: Warning: Integer Underflow.
		return tokenSupply - allocatedSupply
Integer Underflow occurs if:
    allocatedSupply = 57896044618658097711785492504343953926634992332820282019728792003956564819968
INFO:symExec:Flow1
5/5.sol:157:5: Warning: Transaction-Ordering Dependency.
    owner.transfer(_amount)
Flow2
5/5.sol:127:5: Warning: Transaction-Ordering Dependency.
    msg.sender.transfer(ethValue)
INFO:symExec:	====== Analysis Completed ======
```

## PreTgeExperty : 6

max gas:  12328

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 6/6.sol:PreTgeExperty:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 89.5%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): True
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:6/6.sol:86:12: Warning: Integer Overflow.
    assert(txs[txIdx]
Integer Overflow occurs if:
    txs[txIdx] = 32
    txIdx = 30
    founders[msg.sender] = 255
6/6.sol:87:12: Warning: Integer Overflow.
    assert(txs[txIdx]
Integer Overflow occurs if:
    txs[txIdx] = 32
    txs[txIdx].founder = 1461501637330902918203684832716283019655932542975
    txIdx = 30
    founders[msg.sender] = 255
6/6.sol:87:12: Warning: Integer Overflow.
    assert(txs[txIdx].active
Integer Overflow occurs if:
    txs[txIdx] = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    txs[txIdx].founder = 1461501637330902918203684832716283019655932542975
    txIdx = 254
    founders[msg.sender] = 255
6/6.sol:89:5: Warning: Integer Overflow.
    txs[txIdx]
Integer Overflow occurs if:
    txs[txIdx] = 32
    txs[txIdx].active = 255
    txs[txIdx].founder = 1461501637330902918203684832716283019655932542975
    txIdx = 30
    founders[msg.sender] = 255
6/6.sol:89:5: Warning: Integer Overflow.
    txs[txIdx].active
Integer Overflow occurs if:
    txs[txIdx] = 115792089237316195423570985008687907853269984665640554368051027090879731990527
    txs[txIdx].active = 255
    txs[txIdx].founder = 1461501637330902918203684832716283019655932542975
    txIdx = 254
    founders[msg.sender] = 255
6/6.sol:90:5: Warning: Integer Overflow.
    txs[txIdx]
Integer Overflow occurs if:
    txs[txIdx] = 32
    txs[txIdx].active = 255
    txs[txIdx].founder = 1461501637330902918203684832716283019655932542975
    txIdx = 30
    founders[msg.sender] = 255
6/6.sol:90:5: Warning: Integer Overflow.
    txs[txIdx].destAddr
Integer Overflow occurs if:
    txs[txIdx] = 115792089237316195423570985008687907853269984665640554368051027090879731990527
    txs[txIdx].active = 255
    txs[txIdx].founder = 1461501637330902918203684832716283019655932542975
    txIdx = 254
    founders[msg.sender] = 255
6/6.sol:15:3: Warning: Integer Overflow.
  Contributor[] public contributors
6/6.sol:133:11: Warning: Integer Overflow.
      if (contributors[i]
Integer Overflow occurs if:
    contributors.length = 115791205813783806231406193359937536394012070923692126229978523204812483330047
    addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
6/6.sol:135:19: Warning: Integer Overflow.
          return (contributors[i]
Integer Overflow occurs if:
    contributors.length = 12
    contributors[i].addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    idx = 0
6/6.sol:135:19: Warning: Integer Overflow.
          return (contributors[i].amount
Integer Overflow occurs if:
    contributors.length = 12
    contributors[i].addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    idx = 0
6/6.sol:135:43: Warning: Integer Overflow.
          return (contributors[i].amount, contributors[i]
Integer Overflow occurs if:
    contributors.length = 12
    contributors[i].addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    idx = 0
6/6.sol:135:43: Warning: Integer Overflow.
          return (contributors[i].amount, contributors[i].timestamp
Integer Overflow occurs if:
    contributors.length = 12
    contributors[i].addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    idx = 0
6/6.sol:135:70: Warning: Integer Overflow.
          return (contributors[i].amount, contributors[i].timestamp, contributors[i]
Integer Overflow occurs if:
    contributors.length = 12
    contributors[i].addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    idx = 0
6/6.sol:135:70: Warning: Integer Overflow.
          return (contributors[i].amount, contributors[i].timestamp, contributors[i].rejected
Integer Overflow occurs if:
    contributors.length = 12
    contributors[i].addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
    idx = 0
6/6.sol:46:12: Warning: Integer Overflow.
    assert(contributors[idx]
Integer Overflow occurs if:
    idx = 7237005577332262213973186563042994240829374041602535252466099000494570602496
    contributors[idx] = 7237005577332262213973186563042994240829374041602535252466099000494570602497
    managerAddr = 0
6/6.sol:48:13: Warning: Integer Overflow.
    assert(!contributors[idx]
Integer Overflow occurs if:
    idx = 7237005577332262213973186563042994240829374041602535252466099000494570602496
    contributors[idx].addr = 1461501637330902918203684832716283019655932542975
    contributors[idx] = 7237005577332262213973186563042994240829374041602535252466099000494570602497
    managerAddr = 0
6/6.sol:48:13: Warning: Integer Overflow.
    assert(!contributors[idx].rejected
Integer Overflow occurs if:
    idx = 0
    contributors[idx].addr = 1461501637330902918203684832716283019655932542975
    contributors[idx] = 1
    managerAddr = 0
6/6.sol:51:19: Warning: Integer Overflow.
    isWhitelisted[contributors[idx]
Integer Overflow occurs if:
    idx = 7237005577332262213973186563042994240829374041602535252466099000494570602496
    contributors[idx].rejected = 0
    contributors[idx].addr = 1461501637330902918203684832716283019655932542975
    contributors[idx] = 7237005577332262213973186563042994240829374041602535252466099000494570602497
    managerAddr = 0
6/6.sol:54:5: Warning: Integer Overflow.
    contributors[idx]
Integer Overflow occurs if:
    idx = 7237005577332262213973186563042994240829374041602535252466099000494570602496
    contributors[idx].rejected = 0
    contributors[idx].addr = 1461501637330902918203684832716283019655932542975
    contributors[idx] = 7237005577332262213973186563042994240829374041602535252466099000494570602497
    managerAddr = 0
6/6.sol:54:5: Warning: Integer Overflow.
    contributors[idx].rejected
Integer Overflow occurs if:
    idx = 0
    contributors[idx].rejected = 0
    contributors[idx].addr = 1461501637330902918203684832716283019655932542975
    contributors[idx] = 1
    managerAddr = 0
6/6.sol:57:5: Warning: Integer Overflow.
    contributors[idx]
Integer Overflow occurs if:
    idx = 7237005577332262213973186563042994240829374041602535252466099000494570602496
    contributors[idx].rejected = 0
    contributors[idx].addr = 1461501637330902918203684832716283019655932542975
    contributors[idx] = 7237005577332262213973186563042994240829374041602535252466099000494570602497
    managerAddr = 0
6/6.sol:123:11: Warning: Integer Overflow.
      if (contributors[i]
Integer Overflow occurs if:
    contributors.length = 115791205813783806231406193359937536394012070923692126229978523204812483330047
    addr = 0
    contributors[i].addr = 1461501637330902918203684832716283019655932542975
6/6.sol:95:12: Warning: Integer Overflow.
    assert(txs[txIdx]
Integer Overflow occurs if:
    txs[txIdx] = 32
    txIdx = 30
6/6.sol:96:12: Warning: Integer Overflow.
    assert(txs[txIdx]
Integer Overflow occurs if:
    txs[txIdx] = 32
    txs[txIdx].founder = 0
    txIdx = 30
6/6.sol:96:12: Warning: Integer Overflow.
    assert(txs[txIdx].active
Integer Overflow occurs if:
    txs[txIdx] = 115792089129476408754968425830019847505191461971091986349295294083498688643071
    txs[txIdx].founder = 0
    txIdx = 254
6/6.sol:98:5: Warning: Integer Overflow.
    txs[txIdx]
Integer Overflow occurs if:
    txs[txIdx] = 32
    txs[txIdx].active = 255
    txs[txIdx].founder = 0
    txIdx = 30
6/6.sol:98:5: Warning: Integer Overflow.
    txs[txIdx].active
Integer Overflow occurs if:
    txs[txIdx] = 115792089236473697090222515542483150617043915282503098921957783423944887369727
    txs[txIdx].active = 255
    txs[txIdx].founder = 0
    txIdx = 254
6/6.sol:28:3: Warning: Integer Overflow.
  Tx[] public txs
INFO:symExec:Flow1
6/6.sol:90:5: Warning: Transaction-Ordering Dependency.
    txs[txIdx].destAddr.transfer(txs[txIdx].amount)
Flow2
6/6.sol:57:5: Warning: Transaction-Ordering Dependency.
    contributors[idx].addr.transfer(contributors[idx].amount)
INFO:symExec:	====== Analysis Completed ======

```

## ProtectTheCastle : 7
max gas:  9661

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 7/7.sol:ProtectTheCastle:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 44.8%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  True
INFO:symExec:	  Transaction-Ordering Dependence (TOD): True
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:7/7.sol:31:7: Warning: Integer Overflow.
    address[] public citizensAddresses;
    ^
Spanning multiple lines.
7/7.sol:32:7: Warning: Integer Overflow.
    uint[] public citizensAmounts;
    ^
Spanning multiple lines.
INFO:symExec:7/7.sol:75:19: Warning: Callstack Depth Attack Vulnerability.
                citizensAddresses[citizensAddresses.length - 1].send(piggyBank);
                ^
Spanning multiple lines.
7/7.sol:78:19: Warning: Callstack Depth Attack Vulnerability.
                citizensAddresses[citizensAddresses.length - 1].send(piggyBank * 65 / 100);
                ^
Spanning multiple lines.
7/7.sol:79:19: Warning: Callstack Depth Attack Vulnerability.
                citizensAddresses[citizensAddresses.length - 2].send(piggyBank * 35 / 100);
                ^
Spanning multiple lines.
7/7.sol:82:19: Warning: Callstack Depth Attack Vulnerability.
                citizensAddresses[citizensAddresses.length - 1].send(piggyBank * 55 / 100);
                ^
Spanning multiple lines.
7/7.sol:83:19: Warning: Callstack Depth Attack Vulnerability.
                citizensAddresses[citizensAddresses.length - 2].send(piggyBank * 30 / 100);
                ^
Spanning multiple lines.
7/7.sol:84:19: Warning: Callstack Depth Attack Vulnerability.
                citizensAddresses[citizensAddresses.length - 3].send(piggyBank * 15 / 100);
                ^
Spanning multiple lines.
7/7.sol:102:15: Warning: Callstack Depth Attack Vulnerability.
            jester.send(amount * 3 / 100);
            ^
Spanning multiple lines.
7/7.sol:120:15: Warning: Callstack Depth Attack Vulnerability.
            jester.send(amount * 3 / 100);
            ^
Spanning multiple lines.
7/7.sol:126:19: Warning: Callstack Depth Attack Vulnerability.
                citizensAddresses[lastCitizenPaid].send(citizensAmounts[lastCitizenPaid]);
                ^
Spanning multiple lines.
INFO:symExec:Flow1
7/7.sol:65:15: Warning: Transaction-Ordering Dependency.
            msg.sender.send(msg.value - 100 ether);
            ^
Spanning multiple lines.
Flow2
7/7.sol:60:15: Warning: Transaction-Ordering Dependency.
            msg.sender.send(msg.value);
            ^
Spanning multiple lines.
INFO:symExec:	====== Analysis Completed ======
```

## NoFeePonzi : 8
max gas:  529

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 8/8.sol:NoFeePonzi:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 52.0%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  True
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:8/8.sol:14:3: Warning: Integer Overflow.
  Payout[] public payouts
INFO:symExec:8/8.sol:33:7: Warning: Callstack Depth Attack Vulnerability.
      payouts[payoutIndex].addr.send(payouts[payoutIndex].yield)
INFO:symExec:	====== Analysis Completed ======
```

## NamiMultiSigWallet, ERC223ReceivingContract, PresaleToken,  NamiCrowdSale, NamiMarket : 9
max gas:  21793

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 9/9.sol:NamiCrowdSale:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 79.0%
INFO:symExec:	  Integer Underflow: 			 True
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:9/9.sol:409:5: Warning: Integer Underflow.
    string public name = "Nami ICO"
9/9.sol:410:5: Warning: Integer Underflow.
    string public  symbol = "NAC"
9/9.sol:710:9: Warning: Integer Underflow.
        totalSupply -= tokens
Integer Underflow occurs if:
    currentPhase = 3
    balanceOf[_owner] = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    totalSupply = 115792089237316195423570985008687907853269984665640564039457584007913129639934
    crowdsaleManager = 0
INFO:symExec:9/9.sol:578:5: Warning: Integer Overflow.
    function approveAndCall(address _spender, uint256 _value, bytes _extraData)
    ^
Spanning multiple lines.
Integer Overflow occurs if:
    _extraData = 115792089237316195423570985008687907853269984665640564039457584007913129639935
INFO:symExec:	====== Analysis Completed ======
INFO:root:contract 9/9.sol:NamiMarket:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 83.5%
INFO:symExec:	  Integer Underflow: 			 True
INFO:symExec:	  Integer Overflow: 			 False
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): True
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:9/9.sol:1055:5: Warning: Integer Underflow.
    string public name = "Nami Market"
INFO:symExec:Flow1
9/9.sol:1074:13: Warning: Transaction-Ordering Dependency.
            _account.transfer(_amount)
Flow2
9/9.sol:1010:13: Warning: Transaction-Ordering Dependency.
            _to.transfer(_amount)
INFO:symExec:	====== Analysis Completed ======
INFO:root:contract 9/9.sol:NamiMultiSigWallet:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 61.1%
INFO:symExec:	  Integer Underflow: 			 True
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): True
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:9/9.sol:130:26: Warning: Integer Underflow.
        for (uint i=0; i<owners.length - 1
Integer Underflow occurs if:
    owners.length = 0
    isOwner[owner] = 255
9/9.sol:22:5: Warning: Integer Underflow.
    mapping (uint => Transaction) public transactions
9/9.sol:222:17: Warning: Integer Underflow.
            if (transactions[transactionId].destination.call.value(transactions[transactionId].value)(transactions[transactionId].data)
Integer Underflow occurs if:
    transactions[transactionId].destination.call.value(transactions[transactionId].value)(transactions[transactionId].data) = 1
    confirmations[transactionId][owners[i]] = 0
    owners.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    transactions[transactionId].executed = 0
    confirmations[transactionId][owner] = 0
    transactions[transactionId].destination = 1461501637330902918203684832716283019655932542975
    isOwner[owner] = 255
    required = 0
INFO:symExec:9/9.sol:299:69: Warning: Integer Overflow.
            if (pending && !transactions[i].executed || executed && transactions[i].executed
Integer Overflow occurs if:
    executed = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    transactionCount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    pending = 0
9/9.sol:299:29: Warning: Integer Overflow.
            if (pending && !transactions[i].executed
Integer Overflow occurs if:
    pending = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    transactionCount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
9/9.sol:22:5: Warning: Integer Overflow.
    mapping (uint => Transaction) public transactions
9/9.sol:220:13: Warning: Integer Overflow.
            transactions[transactionId].executed
Integer Overflow occurs if:
    confirmations[transactionId][owners[i]] = 0
    owners.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    transactions[transactionId].executed = 0
    confirmations[transactionId][owner] = 0
    transactions[transactionId].destination = 1461501637330902918203684832716283019655932542975
    isOwner[owner] = 255
    required = 0
9/9.sol:222:68: Warning: Integer Overflow.
            if (transactions[transactionId].destination.call.value(transactions[transactionId].value
Integer Overflow occurs if:
    confirmations[transactionId][owners[i]] = 0
    owners.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    transactions[transactionId].executed = 0
    confirmations[transactionId][owner] = 0
    transactions[transactionId].destination = 1461501637330902918203684832716283019655932542975
    isOwner[owner] = 255
    required = 0
9/9.sol:222:103: Warning: Integer Overflow.
            if (transactions[transactionId].destination.call.value(transactions[transactionId].value)(transactions[transactionId].data
Integer Overflow occurs if:
    confirmations[transactionId][owners[i]] = 0
    owners.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    transactions[transactionId].executed = 0
    confirmations[transactionId][owner] = 0
    transactions[transactionId].destination = 1461501637330902918203684832716283019655932542975
    isOwner[owner] = 255
    required = 0
9/9.sol:222:17: Warning: Integer Overflow.
            if (transactions[transactionId].destination.call.value(transactions[transactionId].value)(transactions[transactionId].data)
Integer Overflow occurs if:
    transactions[transactionId].destination.call.value(transactions[transactionId].value)(transactions[transactionId].data) = 115792089237316195423570985008687907853269984665640564039457584007913129639681
    confirmations[transactionId][owners[i]] = 0
    owners.length = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    transactions[transactionId].executed = 0
    confirmations[transactionId][owner] = 0
    transactions[transactionId].destination = 1461501637330902918203684832716283019655932542975
    isOwner[owner] = 255
    required = 0
9/9.sol:179:5: Warning: Integer Overflow.
    function submitTransaction(address destination, uint value, bytes data)
    ^
Spanning multiple lines.
Integer Overflow occurs if:
    data = 115792089237316195423570985008687907853269984665640564039457584007913129639935
INFO:symExec:Flow1
9/9.sol:222:17: Warning: Transaction-Ordering Dependency.
            if (transactions[transactionId].destination.call.value(transactions[transactionId].value)(transactions[transactionId].data)
Flow2
9/9.sol:222:17: Warning: Transaction-Ordering Dependency.
            if (transactions[transactionId].destination.call.value(transactions[transactionId].value)(transactions[transactionId].data)
INFO:symExec:	====== Analysis Completed ======
INFO:root:contract 9/9.sol:SafeMath:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 100.0%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 False
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:	====== Analysis Completed ======
```

## PonzICO : 10
max gas:  52460

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 10/10.sol:PonzICO:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 94.8%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:10/10.sol:86:13: Warning: Integer Overflow.
            invested[msg.sender] += msg.value
Integer Overflow occurs if:
    invested[msg.sender] = 86875982696300330681856535615211295800347953211743057467794207309528289017342
    total = 200000000000000000000000
    investors.length = 0
10/10.sol:88:9: Warning: Integer Overflow.
        total += msg.value
Integer Overflow occurs if:
    total = 57946444636968874474362185532452327156651578984442982355076224432409971834618
    invested[msg.sender] = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    investors.length = 0
10/10.sol:61:9: Warning: Integer Overflow.
        invested[msg.sender] += (dividend + fee)
Integer Overflow occurs if:
    invested[msg.sender] = 94971339064435679133370349063425325215963253791982476507561069026331527708154
    balances[msg.sender] = 71451070938105826937957492733535593933267788156774236937046247274724173250044
    total = 200000000000000000000000
    investors.length = 0
10/10.sol:62:9: Warning: Integer Overflow.
        total += (dividend + fee)
Integer Overflow occurs if:
    total = 108555083659983933209597798445644913612441939852033813908951701836339400916730
    balances[msg.sender] = 65133050195990359925758679067386948167463037146427032110019907403713856126716
    investors.length = 0
10/10.sol:31:13: Warning: Integer Overflow.
            balances[owner] += fee
Integer Overflow occurs if:
    balances[msg.sender] = 113954119566882605020022239214899210903218080147138332864228098547470064090104
    balances[owner] = 87734333487103416919397162500382330975133879750379941255094970025836957105658
    total = 199999999999999999999999
INFO:symExec:	====== Analysis Completed ======
```

## MultiplyX10 : 11
max gas:  617

```
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:root:contract 11/11.sol:MultiplyX10:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 37.4%
INFO:symExec:	  Integer Underflow: 			 True
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  True
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:11/11.sol:27:3: Warning: Integer Underflow.
  string public Message="Welcome Investor! Multiply your ETH Now!"
INFO:symExec:11/11.sol:18:3: Warning: Integer Overflow.
  InvestorArray[] public depositors
INFO:symExec:11/11.sol:54:7: Warning: Callstack Depth Attack Vulnerability.
      depositors[index].EtherAddress.send(payment)
INFO:symExec:	====== Analysis Completed ======
```

## ERC20Basic, ERC20, MerkleMine, MultiMerkleMine : 12, 13

analysis source, compile successfully, segmentation fault
analysis with bytecode

- BytesUtil

max gas:  67

```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 45.5%
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:	====== Analysis Completed ======
```

- ERC20Basic, ERC20, MerkleMine : empty binary

- MerkleMine : oyente error

- MerkleProof

max gas:  67
```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version                                           
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3                                                          
INFO:symExec:   ============ Results ===========
INFO:symExec:     EVM Code Coverage:                     5.3%
INFO:symExec:     Callstack Depth Attack Vulnerability:  False
INFO:symExec:     Transaction-Ordering Dependence (TOD): False
INFO:symExec:     Timestamp Dependency:                  False
INFO:symExec:     Re-Entrancy Vulnerability:             False
INFO:symExec:   ====== Analysis Completed ======
```

- MultiMerkleMine

max gas:  408
```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:symExec:   ============ Results ===========
INFO:symExec:     EVM Code Coverage:                     2.7%
INFO:symExec:     Callstack Depth Attack Vulnerability:  False
INFO:symExec:     Transaction-Ordering Dependence (TOD): False
INFO:symExec:     Timestamp Dependency:                  False
INFO:symExec:     Re-Entrancy Vulnerability:             False
INFO:symExec:   ====== Analysis Completed ======
```

- SafeMath
max gas:  67

```
WARNING:root:You are using an untested version of z3. 4.5.1 is the officially tested version
WARNING:root:You are using evm version 1.8.15. The supported version is 1.7.3
INFO:symExec:   ============ Results ===========
INFO:symExec:     EVM Code Coverage:                     45.5%
INFO:symExec:     Callstack Depth Attack Vulnerability:  False
INFO:symExec:     Transaction-Ordering Dependence (TOD): False
INFO:symExec:     Timestamp Dependency:                  False
INFO:symExec:     Re-Entrancy Vulnerability:             False
INFO:symExec:   ====== Analysis Completed ======
```

## PointEX : 16
max gas:  12311

```
INFO:root:contract 16/16.sol:PointEX:
INFO:symExec:	============ Results ===========
INFO:symExec:	  EVM Code Coverage: 			 44.2%
INFO:symExec:	  Integer Underflow: 			 False
INFO:symExec:	  Integer Overflow: 			 True
INFO:symExec:	  Parity Multisig Bug 2: 		 False
INFO:symExec:	  Callstack Depth Attack Vulnerability:  False
INFO:symExec:	  Transaction-Ordering Dependence (TOD): False
INFO:symExec:	  Timestamp Dependency: 		 False
INFO:symExec:	  Re-Entrancy Vulnerability: 		 False
INFO:symExec:16/16.sol:46:5: Warning: Integer Overflow.
    function transfer(string _fromCompany, string _fromID, uint256 _fromAmounts, string _toCompany, string _toID, uint256 _toAmounts) public onlyDistributor returns (bool) {
    ^
Spanning multiple lines.
Integer Overflow occurs if:
    _fromCompany = 115792089237316195423570985008687907853269984665640564039457584007913129639932
INFO:symExec:	====== Analysis Completed ======
```
