//
//  MainPageController.swift
//  Timer
//
//  Created by Charles on 14-9-27.
//  Copyright (c) 2014年 Charles. All rights reserved.
//

import UIKit

class MainPageController: UIViewController,UIPageViewControllerDelegate{
    
    var pageViewController:UIPageViewController?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.backgroundColor=UIColor.whiteColor()
        // Do any additional setup after loading the view, typically from a nib.
        // Configure the page view controller and add it as a child view controller.
        pageViewController = UIPageViewController(transitionStyle: .Scroll, navigationOrientation: .Horizontal, options: nil)
        pageViewController!.delegate = self
        pageViewController?.dataSource=modelController
        
        var startingViewController=storyboard?.instantiateViewControllerWithIdentifier("ViewController") as ViewController
        var viewControllers=[startingViewController]
        pageViewController!.setViewControllers(viewControllers, direction: .Forward, animated: false, completion: {done in})
        
        
        
        self.addChildViewController(pageViewController!)
        self.view.addSubview(pageViewController!.view)
        
        pageViewController?.didMoveToParentViewController(self)
        
        self.view.gestureRecognizers=self.pageViewController?.gestureRecognizers
        
    }
    
    func change(){
        let secondViewController=storyboard?.instantiateViewControllerWithIdentifier("SecondViewController") as SecondViewController
        var viewControlls=[secondViewController]
        pageViewController?.setViewControllers(viewControlls, direction: .Forward, animated: false, completion: {done in})
        
    }
    var _modelController: ModelController? = nil
    var modelController: ModelController {
        // Return the model controller object, creating it if necessary.
        // In more complex implementations, the model controller may be passed to the view controller.
        if _modelController == nil {
            _modelController = ModelController()
            }
            return _modelController!
            
    }
    
}
