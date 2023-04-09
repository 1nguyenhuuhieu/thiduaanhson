/**
 * @license Copyright (c) 2003-2022, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
};

CKEDITOR.on('instanceReady', function (ev) {
	ev.editor.dataProcessor.htmlFilter.addRules(
	 {
		elements:
		 {
		   $: function (element) {
			 // check for the tag name
			 if (element.name == 'img') {
 
				 element.attributes.class = "img-fluid" // Put your class name here
			 }
 
			 // return element with class attribute
			 return element;
		  }
		}
	});
  });