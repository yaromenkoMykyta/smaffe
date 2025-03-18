// src/app/api.service.ts

import {inject, Injectable} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Config } from '../../environment/config';


type RequestOptions = Parameters<HttpClient['get']>[1];


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private http = inject(HttpClient);

  private baseUrl = Config.backendUrl;

  private defaultOptions = {
    withCredentials: true,
  } as const satisfies RequestOptions;

  put<T>(url: string, body: unknown, options?: Parameters<HttpClient['put']>[2]) {
    return this.http.put<T>(this.baseUrl + url, body, { ...this.defaultOptions, ...options });
  }

  post<T>(url: string, body: unknown, options?: Parameters<HttpClient['post']>[2]) {
    return this.http.post<T>(this.baseUrl + url, body, { ...this.defaultOptions, ...options });
  }

  patch<T>(url: string, body: unknown, options?: Parameters<HttpClient['patch']>[2]) {
    return this.http.patch<T>(this.baseUrl + url, body, { ...this.defaultOptions, ...options });
  }

  get<T>(url: string, options?: Parameters<HttpClient['get']>[1]) {
    return this.http.get<T>(this.baseUrl + url, { ...this.defaultOptions, ...options });
  }

  delete<T>(url: string, options?: Parameters<HttpClient['delete']>[1]) {
    return this.http.delete<T>(this.baseUrl + url, { ...this.defaultOptions, ...options });
  }
}
