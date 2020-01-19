const bookmarkComp = (function (){
	//accept two html files as input, one as the 'original' and one as the 'modified'
	const originalFile;
	const modifiedFile;

	//function: extract href attributes from arbitrary file & create a data structure to hold them
	function extractURLs(bkmrkFile) {

	}

	/* function: Compare the extracted values of both files
	 * (1) list urls present in the 'original' but not in the 'modified' under 'Removed'
	 * (2) list urls present in the 'modified' but not in the 'original' under 'Added'
	 */
	function urlComp() {
		const original = extractURLs(originalFile);
		const modified = extractURLs(modifiedFile);

		const removed;
		const added;
	}
}());