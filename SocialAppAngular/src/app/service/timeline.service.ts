import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { PostResponse } from '../model/post-response';
import { Tag } from '../model/tag';

@Injectable({
	providedIn: 'root'
})
export class TimelineService {
	private host = environment.apiUrl;

	constructor(private httpClient: HttpClient) { }

	getTimelinePosts(page: number, size: number): Observable<any> {
		const reqParams = new HttpParams().set('page', page).set('size', size);
		return this.httpClient.get<PostResponse[] | any | HttpErrorResponse>(`${this.host}/user1/`, { params: reqParams });
	}

	getTimelineTags(): Observable<any> {
		return this.httpClient.get<Tag[] | any | HttpErrorResponse>(`${this.host}/tags/`);
	}
}
