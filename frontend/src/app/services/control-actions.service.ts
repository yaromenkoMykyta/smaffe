import {inject, Injectable} from '@angular/core';
import {ApiService} from './api.service';
import {HttpClientModule} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ControlActionsService {
  private apiService = inject(ApiService)
  constructor() { }

  public make_cream() : void{

    this.apiService.post('actions/make_cream_caffe', []).subscribe(

    );
  }
    public make_espresso() : void{

    this.apiService.post('actions/make_espresso', []).subscribe(

    );
  }
}
