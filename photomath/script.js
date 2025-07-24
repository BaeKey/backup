/*
 Copyright 2024 Blueagle

 Email: austinliu@blueagle.top
 Website: https://blueagle.top

 SPDX-License-Identifier: Proprietary

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software to use the software in its original, unmodified form, subject to the following conditions:

 Reproduction, redistribution, modification, or use in another project is permitted with full credit to the original author. This license and copyright notice must be included.

 This notice and the following disclaimer must be retained in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
function a(d,c){var g=h;if(0!==d.length){var b=g.g,f=d.pop();for(var e of d){if("object"!==typeof b[e]||null===b[e])b[e]={};b=b[e]}e=b[f];c="function"===typeof c?c(e):c;void 0===c?(delete b[f],g.c.delete(d.concat(f).join())):(b[f]=c,g.c.set(d.concat(f).join(),c))}}var l=class{constructor(){this.g=k;this.c=new Map}get h(){return this.g}get i(){return JSON.stringify(this.h)}};const m=$response.body?.toString();var n;try{n=JSON.parse(m||"{}")}catch(d){n={}}const k=n,h=new l;a(["content","tier","added"],"1970-01-08T19:05:42.540Z");a(["content","tier","level"],"genius");a(["content","scope"],["free:solution","paid:solution","trial:solution","mypedia:solution","wip:basic"]);a(["content","subscription","autoRenewing"],!0);a(["content","subscription","expiry"],"2099-01-15T19:07:03.000Z");a(["content","subscription","inGracePeriod"],!1);
a(["content","subscription","orderId"],"320000813070599");a(["content","subscription","packageName"],"com.microblink.PhotoMath");a(["content","subscription","productId"],"com.microblink.PhotoMath.purchase.genius.one_year");a(["content","subscription","started"],"1970-01-08T19:07:03.000Z");a(["content","subscription","status"],"active");a(["content","rewardVideoAdCounter"],3);a(["content","subscriptionSharing"]);a(["content","NotationOne"]);a(["content","freeSunday"]);a(["content","freeSundayVariant"]);
$done({body:h.i});
