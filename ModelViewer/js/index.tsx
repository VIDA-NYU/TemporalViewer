import React from 'react';
import ReactDOM from 'react-dom/client';
import { ModelView} from './ModelView';
import "regenerator-runtime/runtime";

export function renderDatasetsSummarizerBundle(divName: any, dataset_results: any, similarity_metrics: any){
	console.log(divName);
	
	const root = ReactDOM.createRoot(
		document.getElementById(divName) as HTMLElement
	);
	root.render(
		<ModelView sessionInfo={dataset_results['dataset']}/>
	)
}