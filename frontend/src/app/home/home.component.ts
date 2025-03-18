import { Component } from '@angular/core';
import { ToolBarComponent } from '../tool-bar/tool-bar.component';

@Component({
  selector: 'app-home',
  imports: [ToolBarComponent],
  templateUrl: './home.component.html',
  standalone: true,
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
