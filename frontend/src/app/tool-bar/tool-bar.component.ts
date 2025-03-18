import {Component, inject} from '@angular/core';
import { ControlActionsService } from '../services/control-actions.service';

@Component({
  selector: 'app-tool-bar',
  imports: [],
  templateUrl: "./tool-bar.component.html",
  standalone: true,
  styleUrl: './tool-bar.component.css'
})
export class ToolBarComponent {
  private starter: ControlActionsService = inject(ControlActionsService)
  constructor() { }

  ngOnInit(): void {
    // Any initialization logic can go here
  }
  makeCream() : void {
    this.starter.make_cream()
  }
  makeEspresso() : void {
    this.starter.make_espresso()
  }
}
