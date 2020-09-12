from coincurve import PublicKey
from sha3 import keccak_256
import os
myadr =["c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
"742d35cc6634c0532925a3b844bc454e4438f44e",
"be0eb53f46cd790cd13851d5eff43d12404d33e8",
"dc76cd25977e0a5ae17155770273ad58648900d3",
"53d284357ec70ce289d6d64134dfac8e511c8a3d",
"ab7c74abc0c4d48d1bdad5dcb26153fc8780f83e",
"4ddc2d193948926d02f9b1fe9e1daa0718270ed5",
"07ee55aa48bb72dcc6e9d78256648910de513eca",
"e853c56864a2ebe4576a807d26fdc4a0ada51919",
"61edcdf5bb737adffe5043706e7c5bb1f1a56eea",
"229b5c097f9b35009ca1321ad2034d4b3d5070f6",
"73bceb1cd57c711feac4224d062b0f6ff338501e",
"de0b295669a9fd93d5f28d9ec85e40f4cb697bae",
"1b3cb81e51011b549d78bf720b0d924ac763a7c2",
"7d6149ad9a573a6e2ca6ebf7d4897c1b766841b4",
"e92d1a43df510f82c66382592a047d288f85226f",
"66f820a414680b5bcda5eeca5dea238543f42054",
"b4cd0386d2db86f30c1a11c2b8c4f4185c1dade9",
"558553d54183a8542f7832742e7b4ba9c33aa1e6",
"ab5801a7d398351b8be11c439e05c5b3259aec9b",
"ca8fa8f0b631ecdb18cda619c4fc9d197c8affca",
"3bfc20f0b9afcace800d73d2191166ff16540258",
"9a9bed3eb03e386d66f8a29dc67dc29bbb1ccb72",
"059799f2261d37b829c2850cee67b5b975432271",
"1e2fcfd26d36183f1a5d90f0e6296915b02bcb40",
"8103683202aa8da10536036edef04cdd865c225e",
"850c0224f37f67c471e860375ac8e39fea61e8b0",
"0a4c79ce84202b03e95b7a692e5d728d83c44c76",
"189b9cbd4aff470af2c0102f365fc1823d857965",
"e0f5b79ef9f748562a21d017bb7a6706954b7585",
"2b6ed29a95753c3ad948348e3e7b1a251080ffb9",
"d793281182a0e3e023116004778f45c29fc14f19",
"8cf23cd535a240eb0ab8667d24eedbd9eccd5cba",
"267be1c1d684f78cb4f6a176c4911b741e4ffdc0",
"6093d9194a82f86b11a6ac626ac8d0e6b4b4c863",
"6262998ced04146fa42253a5c0af90ca02dfd2a3",
"7da82c7ab4771ff031b66538d2fb9b0b047f6cf9",
"f977814e90da44bfa03b6295a0616a897441acec",
"a7e4fecddc20d83f36971b67e13f1abc98dfcfa6",
"98ec059dc3adfbdd63429454aeb0c990fba4a128",
"1ffedd7837bcbc53f91ad4004263deb8e9107540",
"657e46adad8be23d569ba3105d7a02124e8def97",
"73263803def2ac8b1f8a42fac6539f5841f4e673",
"40f0d6fb7c9ddd9cbc1c02a208380c08cf77189b",
"6047a74d635262fb73ebce6c12bb6b14b3da70b4",
"ea9d571077e7f342f7e8c9bff7f8d06b1212082d",
"78b96178e7ae1ff9adc5d8609e000811657993c8",
"d65bd7f995bcc3bdb2ea2f8ff7554a61d1bf6e53",
"1a71b118ac6c9086f43bcf2bb6ada3393be82a5c",
"fc39f0dc7a1c5d5cd1cdf3b460d5fa99a56abf65",
"d44023d2710dd7bef797a074ecec4fc74fdd52b2",
"7712bdab7c9559ec64a1f7097f36bc805f51ff1a",
"024861e9f89d44d00a7ada4aa89fe03cab9387cd",
"90a9e09501b70570f9b11df2a6d4f047f8630d6d",
"b8808f9e9b88497ec522304055cd537a0913f6a0",
"bf3aeb96e164ae67e763d9e050ff124e7c3fdd28",
"fd61352232157815cf7b71045557192bf0ce1884",
"af10cc6c50defff901b535691550d7af208939c5",
"745a45aee9b15efcf2961617e5e107f7106841ba",
"f274483d5bb6e2522afea3949728f870ba32bb9c",
"5b5b69f4e0add2df5d2176d7dbd20b4897bc7ec4",
"4c766def136f59f6494f0969b1355882080cf8e0",
"3ba25081d3935fcc6788e6220abcace39d58d95d",
"85879ab205ecd05380a429585950ba91decde9c5",
"fd898a0f677e97a9031654fc79a27cb5e31da34a",
"4b4a011c420b91260a272afd91e54accdafdfc1d",
"a8dcc0373822b94d7f57326be24ca67bafcaad6b",
"844ada2ed8ecd77a1a9c72912df0fcb8b8c495a7",
"9c2fc4fc75fa2d7eb5ba9147fa7430756654faa9",
"b20411c403687d1036e05c8a7310a0f218429503",
"9a1ed80ebc9936cee2d3db944ee6bd8d407e7f9f",
"b8cda067fabedd1bb6c11c626862d7255a2414fe",
"b9fa6e54025b4f0829d8e1b42e8b846914659632",
"701c484bfb40ac628afa487b6082f084b14af0bd",
"ba18ded5e0d604a86428282964ae0bb249ceb9d0",
"fe01a216234f79cfc3bea7513e457c6a9e50250d",
"0c05ec4db907cfb91b2a1a29e7b86688b7568a6d",
"c4cf565a5d25ee2803c9b8e91fc3d7c62e79fe69",
"e04cf52e9fafa3d9bf14c407afff94165ef835f7",
"77afe94859163abf0b90725d69e904ea91446c7b",
"19d599012788b991ff542f31208bab21ea38403e",
"ca582d9655a50e6512045740deb0de3a7ee5281f",
"d05e6bf1a00b5b4c9df909309f19e29af792422b",
"0f00294c6e4c30d9ffc0557fec6c586e6f8c3935",
"eb2b00042ce4522ce2d1aacee6f312d26c4eb9d6",
"7ae92148e79d60a0749fd6de374c8e81dfddf792",
"554f4476825293d4ad20e02b54aca13956acc40a",
"9cf36e93a8e2b1eaaa779d9965f46c90b820048c",
"4756eeebf378046f8dd3cb6fa908d93bfd45f139",
"091933ee1088cdf5daace8baec0997a4e93f0dd6",
"a0efb63be0db8fc11681a598bf351a42a6ff50e0",
"8b83b9c4683aa4ec897c569010f09c6d04608163",
"550cd530bc893fc6d2b4df6bea587f17142ab64e",
"828103b231b39fffce028562412b3c04a4640e64",
"367989c660881e1ca693730f7126fe0ffc0963fb",
"e35b0ef92452c353dbb93775e0df97cedf873c72",
"0518f5bb058f6215a0ff5f4df54dae832d734e04",
"0e86733eab26cfcc04bb1752a62ec88e910b4cf5",
"0ff64c53d295533a37f913bb78be9e2adc78f5fe",
"b8b6fe7f357adeab950ac6c270ce340a46989ce1"]
while True:
    private_key=keccak_256(os.urandom(80)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    addr=addr.hex()
    private_key=private_key.hex()
    if addr in str(myadr):
     f=open("foooonddd.txt","a")
     f.write(" add: "+str(addr)+" pk "+str(private_key)+"\n")
     f.close()


